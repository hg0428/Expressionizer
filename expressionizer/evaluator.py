import builtins
import inspect
import json
import math
import sys
from dataclasses import dataclass, field
from typing import Any, Callable, Literal, Optional, Union

from .expression import (
    FunctionCall,
    MathFunction,
    Derivative,
    Integral,
    Numerical,
    Power,
    Product,
    Sum,
    Symbol,
    is_int_or_float,
    numerical_sort_key,
    numerical_sort_key_reverse,
    power,
    product,
    sum,
    derivative,
)
from .number_format import to_trimmed_decimal_string
from .localization import ExplanationProfile, Localizer
from .render import render_latex, render_type


class MathDomainError(ValueError):
    """Custom exception for math domain errors that stores the problematic expression."""

    def __init__(self, message, expression):
        super().__init__(message)
        self.expression = expression


from expressionizer.expression import (
    Product,
    Sum,
    Symbol,
    numerical_sort_key,
    numerical_sort_key_reverse,
    power,
    sum,
    product,
    FunctionCall,
    MathFunction,
    Derivative,
    Integral,
    is_int_or_float,
    derivative,
)
from expressionizer.render import render_latex, render_type
import inspect


def get_caller_line():

    return frame.f_lineno, frame.f_code.co_filename


def round_sig(x, sig=2):
    if x == 0:
        return 0  # Zero is a special case
    return round(x, sig - int(math.floor(math.log10(abs(x)))) - 1)


@dataclass
class WordingOptions:
    templates: dict[str, str] = field(default_factory=dict)
    concise_templates: dict[str, str] = field(default_factory=dict)
    step_heading_template: str = "## {number}"


@dataclass
class CalculatorModeOptions:
    enabled: bool = True
    addition_operand_complexity_threshold: int = 14
    subtraction_operand_complexity_threshold: int = 14
    multiplication_operand_complexity_threshold: int = 8
    power_base_complexity_threshold: int = 5
    power_exponent_complexity_threshold: int = 3
    result_complexity_threshold: int = 28
    template: str = "$$ {expression} = {result} $$"
    concise_template: str = "$$ {expression} = {result} $$"
    operation_templates: dict[str, str] = field(default_factory=dict)
    concise_operation_templates: dict[str, str] = field(default_factory=dict)


@dataclass
class ExplanationEvent:
    rule_id: str
    category: str
    input_expr: Optional[Numerical] = None
    output_expr: Optional[Numerical] = None
    message: Optional[str] = None
    metadata: dict[str, Any] = field(default_factory=dict)
    quality_flags: list[str] = field(default_factory=list)


@dataclass
class CalculusRule:
    rule_id: str
    category: Literal["derivative", "integral"]
    matches: Callable[[Numerical, Symbol], bool]
    apply: Callable[[Numerical, Symbol], Numerical]


def wording(
    context: "EvaluatorContext",
    key: str,
    verbose: str,
    concise: Optional[str] = None,
    **kwargs,
) -> str:
    style = context.options.wording_style
    concise = concise if concise is not None else verbose
    template = verbose if style == "verbose" else concise
    options = context.options.wording_options
    if options is not None:
        if style == "concise":
            template = (
                options.concise_templates.get(key)
                or options.templates.get(key)
                or template
            )
        else:
            template = options.templates.get(key, template)
    return context.localizer.format(key, template, kwargs)


@dataclass
class EvaluatorOptions:
    implicit_multiplication_limit: int = 12
    implicit_addition_limit: int = 100
    slow_step_addition: bool = True
    expand_powers: bool = True
    expand_power_limit: Optional[int] = None
    max_precision: int = 5
    max_exponent: int = 100
    min_value: float = 1e-6
    max_value: float = 1e6
    clamp_numeric_literals: bool = False
    compact_integer_multiplication: bool = True
    allow_approximation: bool = True
    wording_style: Literal["verbose", "concise"] = "verbose"
    wording_options: Optional[WordingOptions] = None
    show_complexity_explanations: bool = True
    show_decimal_shift_explanations: bool = True
    show_multiplication_table: bool = True
    show_addition_alignment_block: bool = True
    show_place_value_steps: bool = True
    show_addition_value_list: bool = True
    show_rule_name: bool = False
    show_assumptions: bool = False
    explanation_verbosity: Literal["minimal", "normal", "detailed"] = "normal"
    zero_power_zero_policy: Literal["undefined", "one", "zero"] = "undefined"
    overflow_policy: Literal["symbolic", "infinity", "zero"] = "symbolic"
    order_of_magnitude_threshold: Optional[int] = 28
    calculator_mode: CalculatorModeOptions = field(default_factory=CalculatorModeOptions)
    explanation_profile: Optional[ExplanationProfile] = None


def compact_evaluator_options(
    wording_style: Literal["verbose", "concise"] = "concise",
    step_heading_template: str = "## {number}",
    explanation_profile: Optional[ExplanationProfile] = None,
) -> EvaluatorOptions:
    return EvaluatorOptions(
        wording_style=wording_style,
        wording_options=WordingOptions(step_heading_template=step_heading_template),
        explanation_profile=explanation_profile,
        show_complexity_explanations=False,
        show_decimal_shift_explanations=False,
        show_multiplication_table=False,
        show_addition_alignment_block=False,
        show_place_value_steps=False,
        show_addition_value_list=False,
        explanation_verbosity="minimal",
    )


def _int_decimal_digits(value: int) -> int:
    magnitude = abs(value)
    if magnitude == 0:
        return 1
    try:
        return len(str(magnitude))
    except ValueError:
        # Avoid Python's large-int string conversion guard for digit counting.
        return int(magnitude.bit_length() * math.log10(2)) + 1


def _numeric_complexity(value: int | float) -> int:
    if isinstance(value, bool):
        return 1
    if isinstance(value, int):
        return _int_decimal_digits(value)
    if not isinstance(value, float):
        return 0
    if not math.isfinite(value):
        return sys.maxsize
    rendered = to_trimmed_decimal_string(abs(value))
    lowered = rendered.lower()
    if "e" in lowered:
        coefficient, exponent_text = lowered.split("e", 1)
        coefficient_digits = sum(ch.isdigit() for ch in coefficient)
        try:
            exponent = abs(int(exponent_text))
        except ValueError:
            exponent = 0
        return coefficient_digits + exponent
    return sum(ch.isdigit() for ch in rendered)


def _estimate_power_result_complexity(base: int | float, exponent: int | float) -> Optional[int]:
    if not is_int_or_float(base) or not is_int_or_float(exponent):
        return None
    if isinstance(exponent, float) and not exponent.is_integer():
        return None
    exponent_int = int(exponent)
    if exponent_int < 0:
        return None
    magnitude = abs(float(base))
    if magnitude in (0.0, 1.0):
        return 1
    try:
        estimate = int(exponent_int * math.log10(magnitude)) + 1
    except (OverflowError, ValueError):
        return None
    return max(1, estimate)


def _order_of_magnitude_expression(order: int, sign: int = 1) -> Numerical:
    magnitude_expr = power(10, max(0, int(order)))
    if sign < 0:
        return product([-1, magnitude_expr])
    return magnitude_expr


def _format_calculator_message(
    context: "EvaluatorContext",
    operation: str,
    expression: Numerical,
    result: Numerical,
    operands: Optional[list[int | float]] = None,
) -> str:
    calculator = context.options.calculator_mode
    style = context.options.wording_style
    operation_templates = (
        calculator.concise_operation_templates
        if style == "concise"
        else calculator.operation_templates
    )
    base_template = (
        calculator.concise_template if style == "concise" else calculator.template
    )
    template = operation_templates.get(operation, base_template)
    lhs = render_latex(operands[0]) if operands and len(operands) > 0 else ""
    rhs = render_latex(operands[1]) if operands and len(operands) > 1 else ""
    payload = {
        "operation": operation,
        "expression": render_latex(expression),
        "result": render_latex(result),
        "lhs": lhs,
        "rhs": rhs,
    }
    try:
        return template.format(**payload)
    except Exception:
        return context.localizer.format(
            "calculator.fallback",
            "$$ {expression} = {result} $$",
            payload,
        )


def _should_use_calculator_for_binary(
    context: "EvaluatorContext",
    operation: str,
    lhs: int | float,
    rhs: int | float,
    result: Optional[int | float] = None,
) -> bool:
    calculator = context.options.calculator_mode
    if calculator is None or not calculator.enabled:
        return False
    if not is_int_or_float(lhs) or not is_int_or_float(rhs):
        return False
    threshold_by_operation = {
        "addition": calculator.addition_operand_complexity_threshold,
        "subtraction": calculator.subtraction_operand_complexity_threshold,
        "multiplication": calculator.multiplication_operand_complexity_threshold,
    }
    threshold = threshold_by_operation.get(operation, calculator.result_complexity_threshold)
    if max(_numeric_complexity(lhs), _numeric_complexity(rhs)) > threshold:
        return True
    if result is not None and _numeric_complexity(result) > calculator.result_complexity_threshold:
        return True
    return False


def _should_use_calculator_for_power(
    context: "EvaluatorContext",
    base: int | float,
    exponent: int | float,
) -> bool:
    calculator = context.options.calculator_mode
    if calculator is None or not calculator.enabled:
        return False
    if max(
        _numeric_complexity(base),
        _numeric_complexity(exponent),
    ) > max(
        calculator.power_base_complexity_threshold,
        calculator.power_exponent_complexity_threshold,
    ):
        return True
    if _numeric_complexity(base) > calculator.power_base_complexity_threshold:
        return True
    if _numeric_complexity(exponent) > calculator.power_exponent_complexity_threshold:
        return True
    estimate = _estimate_power_result_complexity(base, exponent)
    if estimate is not None and estimate > calculator.result_complexity_threshold:
        return True
    return False


class Snapshot:
    portion: Numerical
    original: Numerical
    previous_tree: Numerical
    full_tree: Numerical
    explanation: Optional[str]
    approximate: bool = False

    def __init__(
        self,
        original,
        portion,
        previous_tree,
        full_tree,
        explanation=None,
        approximate=False,
    ):
        self.original = original
        self.portion = portion
        self.previous_tree = previous_tree
        self.full_tree = full_tree
        self.explanation = explanation
        self.approximate = approximate

    def __eq__(self, other):
        if isinstance(other, Snapshot):
            return (
                self.full_tree == other.full_tree
                and self.explanation == other.explanation
            )
        return self.full_tree == other

    def __ne__(self, other):
        return not self == other

    def __bool__(self):
        return True


class TextSnapshot:
    text: str
    breakpoint: bool

    def __init__(self, text: str, breakpoint: bool = False):
        self.text = text
        self.breakpoint = breakpoint

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.text


class BlockContext:
    trees: list[Numerical]
    context: "EvaluatorContext"

    def __init__(self, trees: list[Numerical], context: "EvaluatorContext"):
        # Work on a private list copy to avoid mutating AST argument lists in-place.
        # In-place mutation can retroactively alter previously saved snapshots.
        self.trees = list(trees)
        self.context = context

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.context.blocks.remove(self)

    def __iter__(self):
        return iter(self.trees)

    def __len__(self):
        return len(self.trees)

    def __getitem__(self, index):
        return self.trees[index]

    def __setitem__(self, index, value):
        self.trees[index] = value

    def __delitem__(self, index):
        del self.trees[index]

    def __contains__(self, item):
        return item in self.trees


class EvaluatorContext:
    substitutions: dict[str, int | float]
    steps: list[str]
    snapshots: list[Numerical]
    current_tree: Numerical
    options: EvaluatorOptions
    error_on_invalid_snap: bool
    error_count: int
    is_approximate: bool
    blocks: list[BlockContext]
    explanation_events: list[ExplanationEvent]
    solve_status: Literal["exact", "partial", "unsolved"]
    reason_code: Optional[str]
    coverage_tags: set[str]
    localizer: Localizer
    localization_diagnostics: dict[str, Any]

    def __init__(
        self,
        tree: Numerical,
        substitutions: Optional[dict[str, int | float]] = None,
        options: Optional[EvaluatorOptions] = None,
        error_on_invalid_snap: bool = True,
    ):
        self.substitutions = substitutions or {}
        self.snapshots = [Snapshot(tree, tree, tree, tree)]
        self.blocks = []
        self.current_tree = tree
        self.original_tree = tree
        self.options = options or EvaluatorOptions()
        self.localizer = Localizer.from_profile(self.options.explanation_profile)
        self.error_on_invalid_snap = error_on_invalid_snap
        self.error_count = 0
        self.is_approximate = False
        self.explanation_events = []
        self.solve_status = "exact"
        self.reason_code = None
        self.coverage_tags = set()
        self.localization_diagnostics = {}

    def add_coverage_tag(self, tag: str):
        if tag:
            self.coverage_tags.add(tag)

    def set_status(
        self,
        status: Literal["exact", "partial", "unsolved"],
        reason_code: Optional[str] = None,
    ):
        rank = {"exact": 0, "partial": 1, "unsolved": 2}
        if rank[status] > rank[self.solve_status]:
            self.solve_status = status
            self.reason_code = reason_code
        elif self.reason_code is None and reason_code is not None:
            self.reason_code = reason_code

    def emit_event(
        self,
        rule_id: str,
        category: str,
        input_expr: Optional[Numerical] = None,
        output_expr: Optional[Numerical] = None,
        message: Optional[str] = None,
        metadata: Optional[dict[str, Any]] = None,
        quality_flags: Optional[list[str]] = None,
        emit_text: bool = False,
    ):
        event = ExplanationEvent(
            rule_id=rule_id,
            category=category,
            input_expr=input_expr,
            output_expr=output_expr,
            message=message,
            metadata=metadata or {},
            quality_flags=quality_flags or [],
        )
        self.explanation_events.append(event)
        self.add_coverage_tag(rule_id)
        if emit_text and message:
            prefix = f"[{rule_id}] " if self.options.show_rule_name else ""
            self.snap(prefix + message, False)

    def snap(
        self,
        original: Union[Numerical, str],
        simplified: Union[Numerical, bool] = None,
        explanation: Optional[str] = None,
        approximate=False,
    ):
        if approximate:
            self.is_approximate = True
        if isinstance(original, str):
            rendered_text = self.localizer.transform_text(original)
            text_snapshot = TextSnapshot(rendered_text, bool(simplified))
            if (
                len(self.snapshots) > 0
                and isinstance(self.snapshots[-1], TextSnapshot)
                and str(self.snapshots[-1]) == str(text_snapshot)
            ):
                return
            self.snapshots.append(text_snapshot)
            return
        if contains(self.current_tree, original) <= 0:
            if self.error_on_invalid_snap:
                raise ValueError(
                    f"Original {render_latex(original)} not found in current tree {render_latex(self.current_tree)}.\n{render_type(self.original_tree)}"
                )
            else:
                self.error_count += 1
                return
        previous = self.current_tree

        new_tree = replace_sub(self.current_tree, original, simplified)

        snapshot = Snapshot(
            original, simplified, previous, new_tree, approximate=approximate
        )
        frame = inspect.currentframe().f_back
        line = frame.f_lineno

        # print(f"Called from line {line}.")
        # print("Old tree:", render_type(previous))
        # print("Original:", render_type(original))
        # print("Simplified:", render_type(simplified))
        # print("New tree:", render_type(new_tree))
        # print("\n")

        for i, block in enumerate(self.blocks):
            for j, tree in enumerate(block.trees):

                block.trees[j] = replace_sub(tree, original, simplified)
                # print(
                #     "block tree convert from to",
                #     render_latex(tree),
                #     render_latex(block.trees[j]),
                # )

        if explanation:
            try:
                snapshot.explanation = explanation.format(
                    snapshot=render_latex(new_tree),
                    previous=render_latex(previous),
                    original=render_latex(original),
                    simplified=render_latex(simplified),
                )
            except (KeyError, ValueError, IndexError):
                # Explanations often contain literal braces from LaTeX.
                # If formatting fails, keep original text instead of crashing.
                snapshot.explanation = explanation
            snapshot.explanation = self.localizer.transform_text(snapshot.explanation)
            self.snapshots.append(snapshot)
        elif snapshot != previous or len(self.snapshots) == 0:
            self.snapshots.append(snapshot)
        self.current_tree = new_tree

    def replace(self, state: Numerical, *args, **kwargs):
        self.current_tree = state
        self.snap(*args, **kwargs)

    def save_state(self):
        return self.current_tree

    def render_expressions(self, snapshots: list[Snapshot]):
        if len(snapshots) == 0:
            return ""

        # Split into coherent rewrite chains so each displayed "=" transition is valid.
        chains: list[list[Snapshot]] = [[snapshots[0]]]
        for snapshot in snapshots[1:]:
            last = chains[-1][-1]
            if snapshot.previous_tree == last.full_tree:
                chains[-1].append(snapshot)
            else:
                chains.append([snapshot])

        rendered_chains: list[str] = []
        for chain in chains:
            deduped_chain: list[Snapshot] = []
            for step in chain:
                if (
                    len(deduped_chain) > 0
                    and step.full_tree == deduped_chain[-1].full_tree
                ):
                    continue
                deduped_chain.append(step)
            if len(deduped_chain) == 0:
                continue
            chain = deduped_chain
            first = chain[0]
            if len(chain) == 1 and first.previous_tree == first.full_tree:
                rendered_chains.append(f"$$ {render_latex(first.full_tree)} $$")
                continue

            text = "$$ "
            text += render_latex(first.previous_tree)
            for snapshot in chain:
                text += " \\\\\n= " + render_latex(snapshot.full_tree)
            text += " $$"
            rendered_chains.append(text)

        return "\n".join(rendered_chains) + ("\n" if rendered_chains else "")

    def render(self):
        def _step_heading(step_number: int) -> str:
            template = self.localizer.template("step.heading", "## {number}")
            options = self.options.wording_options
            prefer_default = False
            if options is not None and getattr(options, "step_heading_template", None):
                template = options.step_heading_template
                prefer_default = True
            template = self.localizer.template(
                "step.heading",
                template,
                prefer_default=prefer_default,
            )
            try:
                return template.format(number=step_number)
            except Exception:
                return f"## {step_number}"

        newline = self.localizer.template("render.newline", "\n")
        substep_joiner = self.localizer.template("render.substep.joiner", newline)
        step_joiner = self.localizer.template("render.step.joiner", newline + newline)
        document_prefix = self.localizer.template("render.document.prefix", "")
        document_suffix = self.localizer.template("render.document.suffix", "")

        steps = [[]]
        consecutive = []
        consecutive_portion = []
        last_consecutive_last = None
        current_portion = None
        previous = None
        previous_is_snapshot = False
        previous_snapshot = None
        for snapshot in self.snapshots:
            is_snapshot = isinstance(snapshot, Snapshot)
            if (
                previous_snapshot
                and is_snapshot
                and contains(previous_snapshot.portion, snapshot.original) > 0
            ):
                if (
                    current_portion
                    and current_portion != previous_snapshot.portion
                    and contains(current_portion, snapshot.original) > 0
                ):
                    current_portion = replace_sub(
                        current_portion,
                        snapshot.original,
                        snapshot.portion,
                    )
                else:
                    current_portion = replace_sub(
                        previous_snapshot.portion,
                        snapshot.original,
                        snapshot.portion,
                    )
                if not consecutive_portion:
                    consecutive_portion.append(previous_snapshot)
                consecutive_portion.append(snapshot)

            elif (
                previous_snapshot
                and is_snapshot
                and contains(snapshot.full_tree, previous_snapshot.portion)
                < contains(previous_snapshot.full_tree, previous_snapshot.original)
            ):
                current_portion = snapshot.portion
                if not consecutive_portion:
                    consecutive_portion.append(previous_snapshot)
                consecutive_portion.append(snapshot)
            elif is_snapshot and not (
                not previous_is_snapshot and (previous and previous.breakpoint)
            ):
                if last_consecutive_last and len(consecutive) > 0:
                    steps[-1].append(
                        self.render_expressions([last_consecutive_last, *consecutive])
                    )
                elif len(consecutive) > 1:
                    steps[-1].append(self.render_expressions(consecutive))
                last_consecutive_last = (
                    consecutive[-1] if len(consecutive) > 0 else None
                )

                steps.append([])
                current_portion = None

                consecutive_portion = []
                consecutive = []
            if isinstance(snapshot, TextSnapshot) or snapshot.explanation:
                if last_consecutive_last and len(consecutive) > 0:
                    steps[-1].append(
                        self.render_expressions([last_consecutive_last, *consecutive])
                    )
                elif len(consecutive) > 1:
                    steps[-1].append(self.render_expressions(consecutive))
                last_consecutive_last = (
                    consecutive[-1] if len(consecutive) > 0 else None
                )
                steps[-1].append(
                    str(snapshot)
                    if isinstance(snapshot, TextSnapshot)
                    else snapshot.explanation + "\n"
                )
                consecutive = []
            else:
                # Only add new expressions that aren't duplicate, and aren't the final result unless chaining
                is_duplicate = (
                    previous_snapshot
                    and snapshot.full_tree == previous_snapshot.full_tree
                )
                is_final = snapshot == self.current_tree
                if (
                    is_duplicate
                    and snapshot.explanation
                    and not consecutive[-1].explanation
                ):
                    # Take the last element off of consecutive and replace it with the new one
                    consecutive.pop()
                    is_duplicate = False

                if not is_duplicate:
                    consecutive.append(snapshot)
            if is_snapshot:
                previous_snapshot = snapshot
            previous = snapshot
            previous_is_snapshot = is_snapshot
        if last_consecutive_last:
            steps[-1].append(
                self.render_expressions([last_consecutive_last, *consecutive])
            )
        elif len(consecutive) > 0:
            steps[-1].append(self.render_expressions(consecutive))
        filtered_steps = []
        for step in steps:
            step = [substep for substep in step if substep != ""]
            if step:
                filtered_steps.append(step)
        if len(filtered_steps) == 1:
            body = substep_joiner.join(filtered_steps[0])
            block = self.localizer.format(
                "render.single_step.block",
                "{body}",
                {
                    "heading": _step_heading(1),
                    "body": body,
                    "number": 1,
                    "newline": newline,
                },
            )
            rendered = document_prefix + block + document_suffix
            self.localization_diagnostics = self.localizer.diagnostics()
            return rendered
        blocks: list[str] = []
        for i, step in enumerate(filtered_steps):
            body = substep_joiner.join(step)
            blocks.append(
                self.localizer.format(
                    "render.step.block",
                    "{heading}{newline}{body}",
                    {
                        "heading": _step_heading(i + 1),
                        "body": body,
                        "number": i + 1,
                        "newline": newline,
                    },
                )
            )
        rendered = document_prefix + step_joiner.join(blocks) + document_suffix
        self.localization_diagnostics = self.localizer.diagnostics()
        return rendered

    def render_document(self) -> dict[str, Any]:
        def _step_heading(step_number: int) -> str:
            template = self.localizer.template("step.heading", "## {number}")
            options = self.options.wording_options
            prefer_default = False
            if options is not None and getattr(options, "step_heading_template", None):
                template = options.step_heading_template
                prefer_default = True
            template = self.localizer.template(
                "step.heading",
                template,
                prefer_default=prefer_default,
            )
            try:
                return template.format(number=step_number)
            except Exception:
                return f"## {step_number}"

        newline = self.localizer.template("render.newline", "\n")
        steps = [[]]
        consecutive = []
        consecutive_portion = []
        last_consecutive_last = None
        current_portion = None
        previous = None
        previous_is_snapshot = False
        previous_snapshot = None
        for snapshot in self.snapshots:
            is_snapshot = isinstance(snapshot, Snapshot)
            if (
                previous_snapshot
                and is_snapshot
                and contains(previous_snapshot.portion, snapshot.original) > 0
            ):
                if (
                    current_portion
                    and current_portion != previous_snapshot.portion
                    and contains(current_portion, snapshot.original) > 0
                ):
                    current_portion = replace_sub(
                        current_portion,
                        snapshot.original,
                        snapshot.portion,
                    )
                else:
                    current_portion = replace_sub(
                        previous_snapshot.portion,
                        snapshot.original,
                        snapshot.portion,
                    )
                if not consecutive_portion:
                    consecutive_portion.append(previous_snapshot)
                consecutive_portion.append(snapshot)

            elif (
                previous_snapshot
                and is_snapshot
                and contains(snapshot.full_tree, previous_snapshot.portion)
                < contains(previous_snapshot.full_tree, previous_snapshot.original)
            ):
                current_portion = snapshot.portion
                if not consecutive_portion:
                    consecutive_portion.append(previous_snapshot)
                consecutive_portion.append(snapshot)
            elif is_snapshot and not (
                not previous_is_snapshot and (previous and previous.breakpoint)
            ):
                if last_consecutive_last and len(consecutive) > 0:
                    steps[-1].append(
                        self.render_expressions([last_consecutive_last, *consecutive])
                    )
                elif len(consecutive) > 1:
                    steps[-1].append(self.render_expressions(consecutive))
                last_consecutive_last = (
                    consecutive[-1] if len(consecutive) > 0 else None
                )
                steps.append([])
                current_portion = None
                consecutive_portion = []
                consecutive = []
            if isinstance(snapshot, TextSnapshot) or snapshot.explanation:
                if last_consecutive_last and len(consecutive) > 0:
                    steps[-1].append(
                        self.render_expressions([last_consecutive_last, *consecutive])
                    )
                elif len(consecutive) > 1:
                    steps[-1].append(self.render_expressions(consecutive))
                last_consecutive_last = (
                    consecutive[-1] if len(consecutive) > 0 else None
                )
                steps[-1].append(
                    str(snapshot)
                    if isinstance(snapshot, TextSnapshot)
                    else snapshot.explanation + "\n"
                )
                consecutive = []
            else:
                is_duplicate = (
                    previous_snapshot
                    and snapshot.full_tree == previous_snapshot.full_tree
                )
                if (
                    is_duplicate
                    and snapshot.explanation
                    and len(consecutive) > 0
                    and not consecutive[-1].explanation
                ):
                    consecutive.pop()
                    is_duplicate = False

                if not is_duplicate:
                    consecutive.append(snapshot)
            if is_snapshot:
                previous_snapshot = snapshot
            previous = snapshot
            previous_is_snapshot = is_snapshot
        if last_consecutive_last:
            steps[-1].append(
                self.render_expressions([last_consecutive_last, *consecutive])
            )
        elif len(consecutive) > 0:
            steps[-1].append(self.render_expressions(consecutive))
        filtered_steps = []
        for step in steps:
            cleaned = [substep for substep in step if substep != ""]
            if cleaned:
                filtered_steps.append(cleaned)

        document_steps: list[dict[str, Any]] = []
        for i, step in enumerate(filtered_steps, 1):
            body = newline.join(step)
            document_steps.append(
                {
                    "index": i,
                    "heading": _step_heading(i),
                    "substeps": step,
                    "body": body,
                }
            )
        rendered = self.render()
        return {
            "schema_version": "explanation_document_v1",
            "solve_status": self.solve_status,
            "reason_code": self.reason_code,
            "is_approximate": self.is_approximate,
            "coverage_tags": sorted(self.coverage_tags),
            "steps": document_steps,
            "rendered": rendered,
        }

    def render_json(self, indent: Optional[int] = 2) -> str:
        return json.dumps(self.render_document(), ensure_ascii=False, indent=indent)

    def render_explanation_events(self):
        if len(self.explanation_events) == 0:
            return ""
        lines = []
        for i, event in enumerate(self.explanation_events, 1):
            line = f"{i}. [{event.category}] {event.rule_id}"
            if event.message:
                line += f" - {event.message}"
            if len(event.quality_flags) > 0:
                line += f" (flags: {', '.join(event.quality_flags)})"
            lines.append(line)
        return "\n".join(lines)

    def block(self, trees: list[Numerical]):
        self.blocks.append(BlockContext(trees, self))
        return self.blocks[-1]


def pad(iterable, size, value=None, side="left"):
    if isinstance(iterable, str):
        pad_value = value if isinstance(value, str) else " "
        length = len(iterable)
        pad_len = max(size - length, 0)
        padding = pad_value * pad_len
        return padding + iterable if side == "left" else iterable + padding
    elif isinstance(iterable, list):
        pad_value = value
        length = len(iterable)
        pad_len = max(size - length, 0)
        padding = [pad_value] * pad_len
        return padding + iterable if side == "left" else iterable + padding
    else:
        raise TypeError("Only str and list types are supported.")


def generate_table(rows: list) -> str:
    if not rows:
        return ""
    # Convert all values to strings
    str_rows = [[str(cell) for cell in row] for row in rows]
    # Transpose for column width calculation
    columns = list(zip(*str_rows))
    col_widths = [max(len(cell) for cell in col) for col in columns]

    def format_row(row):
        return (
            "| "
            + " | ".join(cell.ljust(width) for cell, width in zip(row, col_widths))
            + " |"
        )

    header = format_row(str_rows[0])
    separator = "| " + " | ".join("-" * width for width in col_widths) + " |"
    body = [format_row(row) for row in str_rows[1:]]

    return "\n".join([header, separator] + body)


def get_coefficient_exponent(x):
    if x == 0:
        return 0, 0  # Special case: zero
    if isinstance(x, float) and not math.isfinite(x):
        # Keep non-finite values out of place-value decomposition paths.
        return x, 0

    # Work with positive values, restore sign later
    sign = -1 if x < 0 else 1
    x = abs(x)

    s = to_trimmed_decimal_string(x)

    # If decimal present, move decimal to integer and count how many places moved
    if "." in s:
        integer_part, decimal_part = s.split(".")
        if integer_part == "0":
            # e.g. 0.005 → coeff=5, exp=-3
            first_nonzero = next(i for i, c in enumerate(decimal_part) if c != "0")
            coeff = int(decimal_part[first_nonzero:])
            # Value is coeff * 10^{-len(decimal_part)} after trimming leading zeros.
            exp = -len(decimal_part)
        else:
            # e.g. 3.28 → 328, -2
            coeff = int(integer_part + decimal_part)
            exp = -len(decimal_part)
        return sign * coeff, exp
    else:
        # Integer: remove trailing zeros, count them
        zeros = 0
        num = s
        while num.endswith("0"):
            num = num[:-1]
            zeros += 1
        coeff = int(num)
        return sign * coeff, zeros


def render_number_with_power_of_ten(number: int | float) -> str:
    coefficient, exponent = get_coefficient_exponent(number)
    if coefficient == 0:
        return "$0$"
    return f"${coefficient} \\cdot 10^{{{exponent}}}$"


def decompose_number(n):
    s = to_trimmed_decimal_string(abs(n))
    sign = -1 if n < 0 else 1
    if "." in s:
        int_part, frac_part = s.split(".")
    else:
        int_part, frac_part = s, ""
    result = []
    # Integer part
    for i, digit in enumerate(int_part):
        if digit == "0":
            continue
        power = len(int_part) - i - 1
        value = int(digit) * (10**power) * sign
        result.append(value)
    # Fractional part
    for i, digit in enumerate(frac_part):
        if digit == "0":
            continue
        value = float(f"{digit}e-{i + 1}") * sign
        result.append(value)
    if len(result) == 0:
        return [0]
    return result


def solve_sum(components, context: EvaluatorContext):
    from math import floor

    # ---------- helpers ----------
    def split_parts(s):
        sign = -1 if s.startswith("-") else 1
        if sign == -1:
            s = s[1:]
        if "." in s:
            a, b = s.split(".", 1)
        else:
            a, b = s, ""
        return sign, a, b

    def lpad(s, width):
        return "0" * (width - len(s)) + s

    def rpad(s, width):
        return s + "0" * (width - len(s))

    def format_signed_values(values):
        if len(values) == 0:
            return "0"
        rendered = []
        for index, value in enumerate(values):
            magnitude = abs(value)
            if index == 0:
                rendered.append(f"-{magnitude}" if value < 0 else f"{magnitude}")
            else:
                rendered.append(f"- {magnitude}" if value < 0 else f"+ {magnitude}")
        return " ".join(rendered)

    # ---------- build aligned block ----------
    parts = [split_parts(to_trimmed_decimal_string(x)) for x in components]
    left_max = max(len(a) for sign, a, b in parts)
    right_max = max(len(b) for _, _, b in parts)
    has_decimal = right_max > 0
    has_negative = any(sign == -1 for sign, _, _ in parts)

    lines = []
    signs = []
    for sign, a, b in parts:
        signs.append(sign)
        left = a
        if has_decimal:
            line = lpad(left, left_max) + "." + rpad(b, right_max)
        else:
            line = lpad(left, left_max + right_max)  # behave like old code
        if has_negative and sign == -1:
            line = "-" + line
        elif has_negative:
            line = " " + line
        lines.append(line)

    max_length = len(lines[0]) - 1 if has_negative else len(lines[0])
    # old snapshot (exact behavior retained)
    addition = "```\n" + "\n".join(lines) + "\n```"
    if context.options.show_addition_alignment_block:
        context.snap(addition, False)

    # For backward-compat with your later indexing:
    addition = addition.split("\n")[1:-1]  # trim the fences

    # ---------- power map ----------
    if has_decimal:
        dot_idx = left_max  # same for all lines
        power_for_col = []
        for c in range(max_length):
            if c == dot_idx:
                power_for_col.append(None)
            elif c < dot_idx:
                power_for_col.append(dot_idx - c - 1)
            else:
                power_for_col.append(-(c - dot_idx))
    else:
        power_for_col = [None] * max_length  # will compute like before

    carry = 0
    final = [None] * (max_length)

    for i in range(max_length):
        col = max_length - i - 1  # right to left
        # Decimal point column?
        if has_decimal and col == dot_idx:
            final[col] = "."
            continue

        values = []
        for j in range(len(addition)):
            ch = addition[len(addition) - j - 1][col + (1 if has_negative else 0)]
            if ch.isdigit():
                values.append(int(ch) * signs[len(addition) - j - 1])
        if carry != 0:
            values.append(carry)

        sum_values = sum(values)
        carry = (
            math.floor(sum_values / 10)
            if sum_values > 0
            else math.ceil(sum_values / 10)
        )
        digit = sum_values - carry * 10
        if digit < 0:  # Borrow
            digit += 10
            carry -= 1
        final[col] = digit

        # Determine exponent for snap text
        if has_decimal:
            p = power_for_col[col]
            # Skip dot, p can be None only if no decimal or legacy path
        else:
            p = i  # replicate original integer behavior

        # keep your step text shape
        if p is not None:
            if sum_values == 0 and carry == 0 and len(values) > 1:
                continue
            if len(values) > 1:
                step = f"$10^{{{p}}}$: ${format_signed_values(values)} = {sum_values}$"
            else:
                step = f"$10^{{{p}}}$: ${sum_values}$"
            if carry > 0:
                step += wording(
                    context,
                    "addition_carry_suffix",
                    f", so carry {carry} to the next column.",
                    f", carry {carry}.",
                    carry=carry,
                )
            elif carry < 0:
                step += wording(
                    context,
                    "addition_borrow_suffix",
                    f", so borrow {-carry} from the next column and write {digit} here.",
                    f", borrow {-carry}; digit becomes {digit}.",
                    borrow=-carry,
                    digit=digit,
                )
            if context.options.show_place_value_steps:
                context.snap(step, False)
    # leftover carry
    if carry > 0:
        # put carry to the left of everything (may need more than 1 digit)
        c_str = str(abs(carry))
        final = list(c_str) + final
        if context.options.show_place_value_steps:
            context.snap(
                wording(
                    context,
                    "addition_carry_row",
                    f"$10^{{{p+1}}}$: {carry} (carry from the previous column)",
                    f"$10^{{{p+1}}}$: carry {carry}",
                    power=p + 1,
                    carry=carry,
                ),
                False,
            )
        carry = 0
    result_str = "".join(str(x) for x in final).strip()

    # Convert for return (keep int for old path)
    result = float(result_str) if "." in result_str else int(result_str)
    if carry < 0:
        result = -(-carry * 10 ** (p + 1) - result)
    context.snap(
        wording(
            context,
            "addition_put_together",
            f"Combine the place-value columns to obtain ${result}$.",
            f"Result: ${result}$.",
            result=result,
        ),
        False,
    )
    context.snap(Sum(components), result)
    return result


def add(a, b, context: EvaluatorContext):
    if (
        (isinstance(a, float) and not math.isfinite(a))
        or (isinstance(b, float) and not math.isfinite(b))
    ):
        context.snap(Sum([a, b]), a + b)
        return a + b
    quick_result = a + b
    operation = "subtraction" if is_int_or_float(b) and b < 0 else "addition"
    if _should_use_calculator_for_binary(context, operation, a, b, quick_result):
        expression = Sum([a, b])
        context.snap(
            expression,
            quick_result,
            _format_calculator_message(
                context,
                operation,
                expression,
                quick_result,
                [a, b],
            ),
        )
        return quick_result
    limit = context.options.implicit_addition_limit
    a_coefficient, a_exponent = get_coefficient_exponent(a)
    b_coefficient, b_exponent = get_coefficient_exponent(b)
    if (
        -limit <= a_coefficient <= limit
        and -limit <= b_coefficient <= limit
        or (a_coefficient == 1 or b_coefficient == 1)
    ):
        context.snap(Sum([a, b]), a + b)
        return a + b
    a_components = decompose_number(a)
    b_components = decompose_number(b)
    all_components = a_components + b_components
    if context.options.show_complexity_explanations:
        context.snap(
            wording(
                context,
                "addition_decompose_intro",
                f"Decompose ${a}$ and ${b}$ into place-value components.",
                f"Use place-value decomposition for ${a}$ and ${b}$.",
                a=a,
                b=b,
            ),
            False,
        )
    context.snap(Sum([a, b]), Sum(all_components))
    if context.options.slow_step_addition:
        result = solve_sum(all_components, context)
    else:
        context.snap(Sum(all_components), a + b)
        result = a + b
    context.snap("", True)
    return result


def multiply(a, b, context: EvaluatorContext, quick_compute=True):
    if (
        (isinstance(a, float) and not math.isfinite(a))
        or (isinstance(b, float) and not math.isfinite(b))
    ):
        context.snap(Product([a, b]), a * b)
        return a * b
    threshold = context.options.order_of_magnitude_threshold
    if threshold is not None and is_int_or_float(a) and is_int_or_float(b):
        estimated_digits = _numeric_complexity(a) + _numeric_complexity(b)
        if estimated_digits > threshold:
            sign = -1 if ((a < 0) ^ (b < 0)) else 1
            approx_expr = _order_of_magnitude_expression(estimated_digits - 1, sign)
            context.set_status("partial", "order_of_magnitude_estimation")
            digits_a = _numeric_complexity(a)
            digits_b = _numeric_complexity(b)
            context.snap(
                f"Exact multiplication is too large, so estimate by digit count.",
                False,
            )
            context.snap(
                f"${a}$ has about {digits_a} digits and ${b}$ has about {digits_b} digits.",
                False,
            )
            context.snap(
                f"A product of numbers with {digits_a} and {digits_b} digits has about {estimated_digits - 1} to {estimated_digits} digits.",
                False,
            )
            context.snap(
                Product([a, b]),
                approx_expr,
                f"So we use an order-of-magnitude estimate of ${render_latex(approx_expr)}$.",
                approximate=True,
            )
            return approx_expr
    quick_result = a * b
    if _should_use_calculator_for_binary(
        context,
        "multiplication",
        a,
        b,
        quick_result,
    ):
        expression = Product([a, b])
        context.snap(
            expression,
            quick_result,
            _format_calculator_message(
                context,
                "multiplication",
                expression,
                quick_result,
                [a, b],
            ),
        )
        return quick_result
    limit = context.options.implicit_multiplication_limit
    a_coefficient, a_exponent = get_coefficient_exponent(a)
    b_coefficient, b_exponent = get_coefficient_exponent(b)
    a_is_integer_like = isinstance(a, int) or (isinstance(a, float) and a.is_integer())
    b_is_integer_like = isinstance(b, int) or (isinstance(b, float) and b.is_integer())
    if (
        context.options.compact_integer_multiplication
        and is_int_or_float(a)
        and is_int_or_float(b)
        and a_is_integer_like
        and b_is_integer_like
        and min(abs(int(a)), abs(int(b))) <= limit
    ):
        context.snap(Product([a, b]), a * b)
        return a * b
    if (
        -limit <= a_coefficient <= limit
        and -limit <= b_coefficient <= limit
        or (a_coefficient == 1 or b_coefficient == 1)
    ):
        context.snap(Product([a, b]), a * b)
        return a * b
    a_nearest_round = 10 ** (len(str(a)))
    b_nearest_round = 10 ** (len(str(b)))
    a_round_distance = a_nearest_round - a
    b_round_distance = b_nearest_round - b
    if (
        a_round_distance < limit
        and a > limit
        and a_round_distance < b_round_distance
        and quick_compute
    ):
        context.snap(
            Product([a, b]), Product([Sum([a_nearest_round, -a_round_distance]), b])
        )
        if -limit <= b_coefficient <= limit:
            context.snap(
                Product([Sum([a_nearest_round, -a_round_distance]), b]),
                a * b,
            )
        else:
            context.snap(
                Product([Sum([a_nearest_round, -a_round_distance]), b]),
                Sum([a_nearest_round * b, -Product([a_round_distance, b])]),
            )
            result = multiply(a_round_distance, b, context, quick_compute=False)
            context.snap(
                Sum([a_nearest_round * b, -result]),
                a_nearest_round * b - result,
            )
        return a * b

    elif (
        b_round_distance < limit
        and b > limit
        and b_round_distance < a_round_distance
        and quick_compute
    ):
        # initial snap breaking b into (b_nearest_round - b_round_distance)
        context.snap(
            Product([a, b]), Product([a, Sum([b_nearest_round, -b_round_distance])])
        )

        if -limit <= a_coefficient <= limit:
            # if small coefficient, we can compute directly
            context.snap(
                Product([a, Sum([b_nearest_round, -b_round_distance])]),
                a * b,
            )
        else:
            # otherwise, express as difference of two products
            context.snap(
                Product([a, Sum([b_nearest_round, -b_round_distance])]),
                Sum([a * b_nearest_round, -Product([a, b_round_distance])]),
            )
            # compute the hard part a * b_round_distance
            result = multiply(a, b_round_distance, context, quick_compute=False)
            # show the final subtraction
            context.snap(
                Sum([a * b_nearest_round, -result]),
                a * b_nearest_round - result,
            )

        return a * b
    if context.options.show_complexity_explanations:
        context.snap(
            wording(
                context,
                "multiply_complex_intro",
                f"Compute ${a} \\cdot {b}$ by place-value decomposition: form partial products, then add them.",
                f"Use place-value decomposition for ${a} \\cdot {b}$ and add the partial products.",
                a=a,
                b=b,
            ),
            False,
        )
    if (
        context.options.allow_approximation
        and
        a_exponent < 0
        and len(str(abs(a_coefficient))) > context.options.max_precision
    ):
        a_approx = (
            round_sig(a_coefficient, context.options.max_precision) * 10**a_exponent
        )
        context.snap(
            a,
            a_approx,
            wording(
                context,
                "multiply_approximate_a",
                f"Approximate ${a}$ as ${a_approx}$ to control intermediate precision during multiplication.",
                f"Approximate ${a}$ as ${a_approx}$ for multiplication.",
                a=a,
                approximate=a_approx,
            ),
            approximate=True,
        )
    else:
        a_approx = a
    if (
        context.options.allow_approximation
        and
        b_exponent < 0
        and len(str(abs(b_coefficient))) > context.options.max_precision
    ):
        b_approx = (
            round_sig(b_coefficient, context.options.max_precision) * 10**b_exponent
        )
        if b != a:
            context.snap(
                b,
                b_approx,
                (
                    wording(
                        context,
                        "multiply_approximate_b",
                        f"Approximate ${b}$ as ${b_approx}$ to control intermediate precision during multiplication.",
                        f"Approximate ${b}$ as ${b_approx}$ for multiplication.",
                        b=b,
                        approximate=b_approx,
                    )
                    if b != a
                    else None
                ),
                approximate=True,
            )
    else:
        b_approx = b
    a = a_approx
    b = b_approx
    a_coefficient, a_exponent = get_coefficient_exponent(a)
    b_coefficient, b_exponent = get_coefficient_exponent(b)
    total_exponent = 0
    if a_exponent != 0:
        if context.options.show_decimal_shift_explanations:
            context.snap(
                wording(
                    context,
                    "multiply_decimal_shift_a",
                    f"Rewrite ${a}$ as an integer-scaled value times $10^{{{a_exponent}}}$.",
                    f"Rewrite ${a}$ using $10^{{{a_exponent}}}$ scaling.",
                    a=a,
                    exponent=a_exponent,
                ),
                False,
            )
        total_exponent += a_exponent

    if b_exponent != 0:
        if not (b_coefficient == a_coefficient and b_exponent == a_exponent):
            if context.options.show_decimal_shift_explanations:
                context.snap(
                    wording(
                        context,
                        "multiply_decimal_shift_b",
                        f"Rewrite ${b}$ as an integer-scaled value times $10^{{{b_exponent}}}$.",
                        f"Rewrite ${b}$ using $10^{{{b_exponent}}}$ scaling.",
                        b=b,
                        exponent=b_exponent,
                    ),
                    False,
                )
        total_exponent += b_exponent
    if a != a_coefficient or b != b_coefficient:
        context.snap(
            Product([a, b]),
            Product([a_coefficient, b_coefficient, Power(10, total_exponent)]),
        )
    a = a_coefficient
    b = b_coefficient

    a = int(a)
    b = int(b)
    exact_core_result = a * b
    a_str, b_str = str(a), str(b)
    a_components = decompose_number(a)
    b_components = decompose_number(b)

    rows = [
        [""]
        + [render_number_with_power_of_ten(a_component) for a_component in a_components]
    ]
    grid = []
    max_length = 0
    for b_component in b_components:
        rows.append([render_number_with_power_of_ten(b_component)])
        grid.append([])
        for a_component in a_components:
            result = a_component * b_component
            grid[-1].append(result)
            if len(str(result)) > max_length:
                max_length = len(str(result))
            coefficient, exponent = get_coefficient_exponent(result)
            if coefficient == 0:
                rows[-1].append("$0$")
            else:
                rows[-1].append(f"${coefficient} \\cdot 10^{{{exponent}}}$")

    w = len(a_components)
    h = len(b_components)
    all_components = []
    for d in range(w + h - 1):
        for x in range(d, -1, -1):
            y = d - x
            if x < w and y < h:
                all_components.append(grid[y][x])
    context.snap(Product([a, b]), Product([Sum(a_components), Sum(b_components)]))
    if context.options.show_multiplication_table:
        context.snap(
            wording(
                context,
                "multiply_table_header",
                "\n**Partial-product table:**",
                "\n**Partial products:**",
            ),
            False,
        )
        table = generate_table(rows)
        context.snap(table, False)
    context.snap(Product([Sum(a_components), Sum(b_components)]), Sum(all_components))
    if context.options.slow_step_addition:
        if context.options.show_addition_value_list:
            context.snap(
                wording(
                    context,
                    "multiply_values_list_header",
                    "**Add these partial values by place value:**",
                    "**Values to add:**",
                ),
                False,
            )
        result = solve_sum(all_components, context)
        if result != exact_core_result:
            context.snap(Sum(all_components), exact_core_result)
            result = exact_core_result
        if total_exponent != 0:
            scaled_original = Product([result, Power(10, total_exponent)])
            try:
                scaled_result = result * 10**total_exponent
            except OverflowError:
                # Keep exact symbolic scaling when float conversion would overflow.
                result = scaled_original
            else:
                context.snap(scaled_original, scaled_result)
                result = scaled_result
        context.snap("", True)
        return result
    else:
        result = exact_core_result
        context.snap(Sum(all_components), result)
        if total_exponent != 0:
            scaled_original = Product([result, Power(10, total_exponent)])
            try:
                scaled_result = result * 10**total_exponent
            except OverflowError:
                # Keep exact symbolic scaling when float conversion would overflow.
                result = scaled_original
            else:
                context.snap(scaled_original, scaled_result)
                result = scaled_result
        context.snap("", True)
        return result


def replace_symbols(expression: Numerical, context: EvaluatorContext):
    match expression:
        case Symbol():
            if expression.name in context.substitutions:
                return context.substitutions[expression.name]
            else:
                return expression
        case Product():
            return Product(
                [replace_symbols(factor, context) for factor in expression.factors]
            )
        case Sum():
            return Sum([replace_symbols(term, context) for term in expression.terms])
        case Power():
            return Power(
                replace_symbols(expression.base, context),
                replace_symbols(expression.exponent, context),
            )
        case FunctionCall():
            return expression.function(
                [
                    replace_symbols(arg, context)
                    for arg in expression.functional_arguments
                ],
                [
                    replace_symbols(arg, context)
                    for arg in expression.subscript_arguments
                ],
                [
                    replace_symbols(arg, context)
                    for arg in expression.superscript_arguments
                ],
            )
        case Derivative():
            bound_names = {v.name for v, _ in expression.variables}
            filtered = {
                k: v
                for k, v in context.substitutions.items()
                if not (isinstance(k, str) and k in bound_names)
            }
            inner_context = EvaluatorContext(
                expression.expression,
                filtered,
                options=context.options,
                error_on_invalid_snap=False,
            )
            return Derivative(
                replace_symbols(expression.expression, inner_context),
                expression.variables,
            )
        case Integral():
            filtered = {
                k: v
                for k, v in context.substitutions.items()
                if not (isinstance(k, str) and k == expression.variable.name)
            }
            inner_context = EvaluatorContext(
                expression.expression,
                filtered,
                options=context.options,
                error_on_invalid_snap=False,
            )
            return Integral(
                replace_symbols(expression.expression, inner_context),
                expression.variable,
                replace_symbols(expression.lower, context)
                if expression.lower is not None
                else None,
                replace_symbols(expression.upper, context)
                if expression.upper is not None
                else None,
            )
        case _:
            return expression


def replace_sub(expr, target, replacement):
    """
    Return a *new* expression obtained by replacing `target`
    (a subtree) with `replacement` inside `expr`.
    Works recursively for all node types.
    """
    if expr == target:
        return replacement
    elif expr == -target:
        return -replacement
    match expr:
        case Power():
            return Power(
                replace_sub(expr.base, target, replacement),
                replace_sub(expr.exponent, target, replacement),
            )
        case Product():
            if isinstance(target, Product) and target in expr:
                if isinstance(replacement, Product):
                    new_factors = replacement.factors.copy()
                else:
                    new_factors = [replacement]
                target_factors = []
                expr_factors = []
                expr_sign = 1
                target_sign = 1
                for factor in expr.factors:
                    if isinstance(factor, Product):
                        expr_factors.extend(factor.factors)
                    elif isinstance(factor, Sum) and len(factor.terms) <= 1:
                        expr_factors.extend(factor.terms)
                    elif is_int_or_float(factor):
                        expr_sign *= 1 if factor >= 0 else -1
                        if abs(factor) != 1:
                            expr_factors.append(abs(factor))
                    else:
                        expr_factors.append(factor)
                for factor in target.factors:
                    if isinstance(factor, Product):
                        target_factors.extend(factor.factors)
                    elif isinstance(factor, Sum) and len(factor.terms) == 1:
                        target_factors.append(factor.terms[0])
                    elif is_int_or_float(factor):
                        target_sign *= 1 if factor >= 0 else -1
                        if abs(factor) != 1:
                            target_factors.append(abs(factor))
                    else:
                        target_factors.append(factor)
                for factor in expr_factors:
                    for target_factor in target_factors:
                        if factor == target_factor:
                            target_factors.remove(target_factor)
                            break
                    else:
                        new_factors.append(factor)
                new_sign = expr_sign * target_sign
                if new_sign < 0:
                    new_factors.append(-1)
                if len(target_factors) == 0:
                    if len(new_factors) == 1:
                        return new_factors[0]
                    return Product(new_factors)
            elif (
                len(expr.factors) == 2
                and -1 in expr.factors
                and -target in expr.factors
            ):
                return replacement
            return Product([replace_sub(f, target, replacement) for f in expr.factors])
        case Sum():
            if (
                isinstance(target, Sum) and target in expr
            ):  # Issue here. See error on test.py
                if isinstance(replacement, Sum):
                    new_terms = replacement.terms.copy()
                else:
                    new_terms = [replacement]
                expr_terms = []
                for term in expr.terms:
                    if isinstance(term, Sum):
                        expr_terms.extend(term.terms)
                    # elif isinstance(term, Product) and len(term.factors) == 1:
                    #     expr_terms.append(term.factors[0])
                    elif (
                        isinstance(term, Product)
                        and len(term.factors) == 2
                        and -1 in term.factors
                    ):
                        expr_terms.append(product([term.factors[0], term.factors[1]]))
                    else:
                        expr_terms.append(term)
                target_terms = []
                for term in target.terms:
                    if isinstance(term, Sum):
                        target_terms.extend(term.terms)
                    if isinstance(term, Product) and len(term.factors) == 1:
                        target_terms.append(term.factors[0])
                    elif (
                        isinstance(term, Product)
                        and len(term.factors) == 2
                        and -1 in term.factors
                    ):
                        target_terms.append(product([term.factors[0], term.factors[1]]))
                    else:
                        target_terms.append(term)
                for term in expr_terms:
                    for target_term in target_terms:
                        if term == target_term:
                            target_terms.remove(target_term)
                            break
                    else:
                        new_terms.append(term)
                if len(target_terms) == 0:
                    if len(new_terms) == 1:
                        return new_terms[0]
                    return Sum(new_terms)
            return Sum([replace_sub(t, target, replacement) for t in expr.terms])
        case FunctionCall():
            return FunctionCall(
                expr.function,
                [
                    replace_sub(a, target, replacement)
                    for a in expr.functional_arguments
                ],
                [replace_sub(a, target, replacement) for a in expr.subscript_arguments],
                [
                    replace_sub(a, target, replacement)
                    for a in expr.superscript_arguments
                ],
            )
        case Derivative():
            return Derivative(
                replace_sub(expr.expression, target, replacement),
                [
                    (replace_sub(v, target, replacement), o)
                    for v, o in expr.variables
                ],
            )
        case Integral():
            return Integral(
                replace_sub(expr.expression, target, replacement),
                replace_sub(expr.variable, target, replacement),
                replace_sub(expr.lower, target, replacement)
                if expr.lower is not None
                else None,
                replace_sub(expr.upper, target, replacement)
                if expr.upper is not None
                else None,
            )
        case _:
            return expr  # atom


def contains(expr, target):
    """
    Return a *new* expression obtained by replacing `target`
    (a subtree) with `replacement` inside `expr`.
    Works recursively for all node types.
    """
    if expr == target:
        return 1
    elif expr == -target:
        return 1
    match expr:
        case Power():
            return contains(expr.base, target) + contains(expr.exponent, target)
        case Product():
            if isinstance(target, Product) and target in expr:
                return 1
            return any([contains(f, target) for f in expr.factors])
        case Sum():
            if isinstance(target, Sum) and target in expr:
                return 1
            return any([contains(t, target) for t in expr.terms])
        case FunctionCall():
            return sum(
                [contains(a, target) for a in expr.functional_arguments]
                + [contains(a, target) for a in expr.subscript_arguments]
                + [contains(a, target) for a in expr.superscript_arguments]
            )
        case Derivative():
            return contains(expr.expression, target) + sum(
                [contains(v, target) for v, _ in expr.variables]
            )
        case Integral():
            return (
                contains(expr.expression, target)
                + contains(expr.variable, target)
                + (
                    contains(expr.lower, target)
                    if expr.lower is not None
                    else 0
                )
                + (
                    contains(expr.upper, target)
                    if expr.upper is not None
                    else 0
                )
            )
        case _:
            return 0


def _contains_node_type(expr: Numerical, node_types: tuple[type, ...]) -> bool:
    if isinstance(expr, node_types):
        return True
    match expr:
        case Sum():
            return any(_contains_node_type(term, node_types) for term in expr.terms)
        case Product():
            return any(_contains_node_type(factor, node_types) for factor in expr.factors)
        case Power():
            return _contains_node_type(expr.base, node_types) or _contains_node_type(
                expr.exponent, node_types
            )
        case FunctionCall():
            return any(
                _contains_node_type(arg, node_types)
                for arg in (
                    expr.functional_arguments
                    + expr.subscript_arguments
                    + expr.superscript_arguments
                )
            )
        case Derivative():
            return _contains_node_type(expr.expression, node_types)
        case Integral():
            return (
                _contains_node_type(expr.expression, node_types)
                or (
                    _contains_node_type(expr.lower, node_types)
                    if expr.lower is not None
                    else False
                )
                or (
                    _contains_node_type(expr.upper, node_types)
                    if expr.upper is not None
                    else False
                )
            )
        case _:
            return False


def _get_term_parts(term):
    """Separates a term into its coefficient and variable parts."""
    if isinstance(term, (int, float)):
        return term, 1

    if isinstance(term, Product):
        coefficient = 1
        variable_factors = []
        for factor in term.factors:
            if isinstance(factor, (int, float)):
                coefficient *= factor
            else:
                variable_factors.append(factor)

        if not variable_factors:
            return coefficient, 1
        if len(variable_factors) == 1:
            return coefficient, variable_factors[0]
        return coefficient, Product(variable_factors)

    # For Symbols, Powers, and other expressions, the coefficient is 1
    return 1, term


def get_fraction(expr):
    # Helper: single object to Product([obj])
    def to_product(lst):
        if len(lst) == 1:
            return lst[0]
        else:
            return Product(lst)

    # Case 1: Power
    if isinstance(expr, Power):
        if is_int_or_float(expr.exponent) and expr.exponent < 0:
            numerator = 1
            denominator = Power(expr.base, -expr.exponent)
            return (numerator, denominator)
        else:
            return None

    # Case 2: Product
    if isinstance(expr, Product):
        num_factors = []
        den_factors = []
        for factor in expr.factors:
            if (
                isinstance(factor, Power)
                and is_int_or_float(factor.exponent)
                and factor.exponent < 0
            ):
                den_factors.append(Power(factor.base, -factor.exponent))
            elif factor == 1:
                num_factors.append(factor)  # Keep '1' in numerator (harmless)
            else:
                num_factors.append(factor)

        if den_factors:
            numerator = to_product(num_factors) if num_factors else 1
            denominator = to_product(den_factors)
            return (numerator, denominator)
        else:
            return None

    # Otherwise, not a fraction
    return None


def _contains_symbol(expr: Numerical, variable: Symbol) -> bool:
    match expr:
        case int() | float():
            return False
        case Symbol():
            return expr.name == variable.name
        case Sum():
            return any(_contains_symbol(term, variable) for term in expr.terms)
        case Product():
            return any(_contains_symbol(factor, variable) for factor in expr.factors)
        case Power():
            return _contains_symbol(expr.base, variable) or _contains_symbol(
                expr.exponent, variable
            )
        case FunctionCall():
            return any(_contains_symbol(arg, variable) for arg in expr.functional_arguments) or any(
                _contains_symbol(arg, variable) for arg in expr.subscript_arguments
            ) or any(_contains_symbol(arg, variable) for arg in expr.superscript_arguments)
        case Derivative():
            return _contains_symbol(expr.expression, variable)
        case Integral():
            if expr.variable.name == variable.name:
                return False
            in_bounds = (
                (expr.lower is not None and _contains_symbol(expr.lower, variable))
                or (expr.upper is not None and _contains_symbol(expr.upper, variable))
            )
            return _contains_symbol(expr.expression, variable) or in_bounds
        case _:
            return False


def _substitute_symbol(expr: Numerical, variable: Symbol, value: Numerical) -> Numerical:
    match expr:
        case Symbol():
            return value if expr.name == variable.name else expr
        case Sum():
            return Sum([_substitute_symbol(term, variable, value) for term in expr.terms])
        case Product():
            return Product(
                [_substitute_symbol(factor, variable, value) for factor in expr.factors]
            )
        case Power():
            return Power(
                _substitute_symbol(expr.base, variable, value),
                _substitute_symbol(expr.exponent, variable, value),
            )
        case FunctionCall():
            return FunctionCall(
                expr.function,
                [
                    _substitute_symbol(arg, variable, value)
                    for arg in expr.functional_arguments
                ],
                [_substitute_symbol(arg, variable, value) for arg in expr.subscript_arguments],
                [
                    _substitute_symbol(arg, variable, value)
                    for arg in expr.superscript_arguments
                ],
            )
        case Derivative():
            if any(v.name == variable.name for v, _ in expr.variables):
                return expr
            return Derivative(
                _substitute_symbol(expr.expression, variable, value), expr.variables
            )
        case Integral():
            if expr.variable.name == variable.name:
                return Integral(
                    expr.expression,
                    expr.variable,
                    _substitute_symbol(expr.lower, variable, value)
                    if expr.lower is not None
                    else None,
                    _substitute_symbol(expr.upper, variable, value)
                    if expr.upper is not None
                    else None,
                )
            return Integral(
                _substitute_symbol(expr.expression, variable, value),
                expr.variable,
                _substitute_symbol(expr.lower, variable, value)
                if expr.lower is not None
                else None,
                _substitute_symbol(expr.upper, variable, value)
                if expr.upper is not None
                else None,
            )
        case _:
            return expr


def _diff_match_numeric(expr: Numerical, _: Symbol) -> bool:
    return is_int_or_float(expr)


def _diff_apply_numeric(_: Numerical, __: Symbol) -> Numerical:
    return 0


def _diff_match_symbol(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Symbol)


def _diff_apply_symbol(expr: Numerical, variable: Symbol) -> Numerical:
    return 1 if expr.name == variable.name else 0


def _diff_match_sum(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Sum)


def _diff_apply_sum(expr: Numerical, variable: Symbol) -> Numerical:
    return sum([_differentiate_once(term, variable) for term in expr.terms])


def _diff_match_product(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Product)


def _diff_apply_product(expr: Numerical, variable: Symbol) -> Numerical:
    terms = []
    for i, factor in enumerate(expr.factors):
        d_factor = _differentiate_once(factor, variable)
        if d_factor == 0:
            continue
        new_factors = expr.factors.copy()
        new_factors[i] = d_factor
        terms.append(product(new_factors))
    return sum(terms) if len(terms) > 0 else 0


def _diff_match_power(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Power)


def _diff_apply_power(expr: Numerical, variable: Symbol) -> Numerical:
    base = expr.base
    exponent = expr.exponent
    d_base = _differentiate_once(base, variable)
    d_exponent = _differentiate_once(exponent, variable)
    if is_int_or_float(exponent):
        return product([exponent, power(base, exponent - 1), d_base])
    if d_exponent == 0:
        return product([exponent, power(base, exponent - 1), d_base])
    return product(
        [
            power(base, exponent),
            sum(
                [
                    product(
                        [
                            d_exponent,
                            FunctionCall(MathFunction("ln", functional_parameters=1), [base]),
                        ]
                    ),
                    product([exponent, d_base, power(base, -1)]),
                ]
            ),
        ]
    )


def _diff_match_function(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, FunctionCall)


def _diff_apply_function(expr: Numerical, variable: Symbol) -> Numerical:
    if len(expr.functional_arguments) != 1:
        return derivative(expr, [(variable, 1)])
    arg = expr.functional_arguments[0]
    d_arg = _differentiate_once(arg, variable)
    if d_arg == 0:
        return 0
    name = expr.function.name
    if name == "sin":
        return product([FunctionCall(MathFunction("cos", 1), [arg]), d_arg])
    if name == "cos":
        return product([-1, FunctionCall(MathFunction("sin", 1), [arg]), d_arg])
    if name == "tan":
        return product([power(FunctionCall(MathFunction("sec", 1), [arg]), 2), d_arg])
    if name == "exp":
        return product([FunctionCall(MathFunction("exp", 1), [arg]), d_arg])
    if name == "ln":
        return product([d_arg, power(arg, -1)])
    if name == "sqrt":
        return product(
            [
                d_arg,
                power(2, -1),
                power(FunctionCall(MathFunction("sqrt", 1), [arg]), -1),
            ]
        )
    if name == "log" and len(expr.subscript_arguments) == 1:
        base = expr.subscript_arguments[0]
        if not _contains_symbol(base, variable):
            return product(
                [
                    d_arg,
                    power(arg, -1),
                    power(
                        FunctionCall(MathFunction("ln", functional_parameters=1), [base]),
                        -1,
                    ),
                ]
            )
    return derivative(expr, [(variable, 1)])


def _diff_match_derivative(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Derivative)


def _diff_apply_derivative(expr: Numerical, variable: Symbol) -> Numerical:
    return derivative(expr.expression, expr.variables + [(variable, 1)])


def _diff_match_integral(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Integral)


def _diff_apply_integral(expr: Numerical, variable: Symbol) -> Numerical:
    if expr.lower is None and expr.upper is None and expr.variable.name == variable.name:
        return expr.expression
    return derivative(expr, [(variable, 1)])


def _int_match_constant(expr: Numerical, _: Symbol) -> bool:
    return is_int_or_float(expr)


def _int_apply_constant(expr: Numerical, variable: Symbol) -> Numerical:
    return product([expr, variable])


def _int_match_symbol(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Symbol)


def _int_apply_symbol(expr: Numerical, variable: Symbol) -> Numerical:
    if expr.name == variable.name:
        return product([power(variable, 2), power(2, -1)])
    return product([expr, variable])


def _int_match_sum(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Sum)


def _int_apply_sum(expr: Numerical, variable: Symbol) -> Numerical:
    return sum([_integrate_once(term, variable) for term in expr.terms])


def _int_match_product(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Product)


def _int_apply_product(expr: Numerical, variable: Symbol) -> Numerical:
    constant_factors = []
    variable_factors = []
    for factor in expr.factors:
        if _contains_symbol(factor, variable):
            variable_factors.append(factor)
        else:
            constant_factors.append(factor)
    if len(variable_factors) == 0:
        return product([expr, variable])
    if len(variable_factors) == 1:
        integrated = _integrate_once(variable_factors[0], variable)
        return product(constant_factors + [integrated])
    return Integral(expr, variable)


def _int_match_power(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Power)


def _int_apply_power(expr: Numerical, variable: Symbol) -> Numerical:
    if isinstance(expr.base, Symbol) and expr.base.name == variable.name and is_int_or_float(
        expr.exponent
    ):
        if expr.exponent == -1:
            return FunctionCall(MathFunction("ln", functional_parameters=1), [variable])
        return product(
            [
                power(variable, expr.exponent + 1),
                power(expr.exponent + 1, -1),
            ]
        )
    return Integral(expr, variable)


def _int_match_function(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, FunctionCall)


def _int_apply_function(expr: Numerical, variable: Symbol) -> Numerical:
    if len(expr.functional_arguments) != 1:
        return Integral(expr, variable)
    arg = expr.functional_arguments[0]
    d_arg = _differentiate_once(arg, variable)
    if not is_int_or_float(d_arg) or d_arg == 0:
        return Integral(expr, variable)
    inv = power(d_arg, -1)
    name = expr.function.name
    if name == "sin":
        return product([-1, FunctionCall(MathFunction("cos", 1), [arg]), inv])
    if name == "cos":
        return product([FunctionCall(MathFunction("sin", 1), [arg]), inv])
    if name == "exp":
        return product([FunctionCall(MathFunction("exp", 1), [arg]), inv])
    if name == "ln" and isinstance(arg, Symbol) and arg.name == variable.name:
        return sum(
            [
                product([variable, FunctionCall(MathFunction("ln", 1), [variable])]),
                product([-1, variable]),
            ]
        )
    return Integral(expr, variable)


def _int_match_derivative(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Derivative)


def _int_apply_derivative(expr: Numerical, variable: Symbol) -> Numerical:
    if (
        len(expr.variables) == 1
        and expr.variables[0][0].name == variable.name
        and expr.variables[0][1] == 1
    ):
        return expr.expression
    return Integral(expr, variable)


def _int_match_integral(expr: Numerical, _: Symbol) -> bool:
    return isinstance(expr, Integral)


def _int_apply_integral(expr: Numerical, variable: Symbol) -> Numerical:
    return Integral(expr, variable)


DERIVATIVE_RULES: list[CalculusRule] = [
    CalculusRule("diff_numeric", "derivative", _diff_match_numeric, _diff_apply_numeric),
    CalculusRule("diff_symbol", "derivative", _diff_match_symbol, _diff_apply_symbol),
    CalculusRule("diff_sum", "derivative", _diff_match_sum, _diff_apply_sum),
    CalculusRule("diff_product", "derivative", _diff_match_product, _diff_apply_product),
    CalculusRule("diff_power", "derivative", _diff_match_power, _diff_apply_power),
    CalculusRule("diff_function_chain", "derivative", _diff_match_function, _diff_apply_function),
    CalculusRule("diff_nested_derivative", "derivative", _diff_match_derivative, _diff_apply_derivative),
    CalculusRule("diff_integral", "derivative", _diff_match_integral, _diff_apply_integral),
]


INTEGRAL_RULES: list[CalculusRule] = [
    CalculusRule("int_constant", "integral", _int_match_constant, _int_apply_constant),
    CalculusRule("int_symbol", "integral", _int_match_symbol, _int_apply_symbol),
    CalculusRule("int_sum", "integral", _int_match_sum, _int_apply_sum),
    CalculusRule("int_product_constant_factor", "integral", _int_match_product, _int_apply_product),
    CalculusRule("int_power_rule", "integral", _int_match_power, _int_apply_power),
    CalculusRule("int_function_u_sub", "integral", _int_match_function, _int_apply_function),
    CalculusRule("int_derivative_inverse", "integral", _int_match_derivative, _int_apply_derivative),
    CalculusRule("int_nested_integral", "integral", _int_match_integral, _int_apply_integral),
]


def _apply_calculus_rule(
    expr: Numerical,
    variable: Symbol,
    context: Optional[EvaluatorContext],
    rules: list[CalculusRule],
) -> Optional[Numerical]:
    for rule in rules:
        if rule.matches(expr, variable):
            result = rule.apply(expr, variable)
            if context is not None:
                context.emit_event(
                    rule_id=rule.rule_id,
                    category=rule.category,
                    input_expr=expr,
                    output_expr=result,
                )
            return result
    return None


def _differentiate_once(expr: Numerical, variable: Symbol, context: Optional[EvaluatorContext] = None) -> Numerical:
    if not _contains_symbol(expr, variable):
        if context is not None:
            context.emit_event(
                "diff_constant_by_absence",
                "derivative",
                input_expr=expr,
                output_expr=0,
            )
        return 0

    result = _apply_calculus_rule(expr, variable, context, DERIVATIVE_RULES)
    if result is not None:
        return result

    result = derivative(expr, [(variable, 1)])
    if context is not None:
        context.set_status("partial", "derivative_unsolved_rule")
        context.emit_event(
            "diff_fallback_symbolic",
            "derivative",
            input_expr=expr,
            output_expr=result,
            quality_flags=["unsolved_symbolic"],
        )
    return result


def _integrate_once(expr: Numerical, variable: Symbol, context: Optional[EvaluatorContext] = None) -> Numerical:
    result = _apply_calculus_rule(expr, variable, context, INTEGRAL_RULES)
    if result is not None:
        return result

    fallback = Integral(expr, variable)
    if context is not None:
        context.set_status("partial", "integral_unsolved_rule")
        context.emit_event(
            "int_fallback_symbolic",
            "integral",
            input_expr=expr,
            output_expr=fallback,
            quality_flags=["unsolved_symbolic"],
        )
    return fallback


def evaluate_expression(expression: Numerical, context: EvaluatorContext):

    result = None
    match expression:
        case int() | float():
            if abs(expression) < context.options.min_value:
                result = 0
            elif (
                context.options.clamp_numeric_literals
                and expression > context.options.max_value
            ):
                result = float("inf")
            elif (
                context.options.clamp_numeric_literals
                and expression < -context.options.max_value
            ):
                result = float("-inf")
            else:
                result = expression

            if result != expression:
                context.snap(expression, result)
        case Power():
            with context.block([expression.exponent]) as block:
                base = evaluate_expression(expression.base, context)
                exponent = block[0]
            if base == 0:
                preview_context = EvaluatorContext(
                    exponent,
                    context.substitutions,
                    options=context.options,
                    error_on_invalid_snap=False,
                )
                preview_exponent = evaluate_expression(exponent, preview_context)
                if is_int_or_float(preview_exponent):
                    if preview_exponent == 0:
                        match context.options.zero_power_zero_policy:
                            case "one":
                                context.snap(
                                    expression,
                                    1,
                                    wording(
                                        context,
                                        "zero_power_zero_one",
                                        "$0^0$ is configured to evaluate to $1$.",
                                        "$0^0 \\rightarrow 1$ by configuration.",
                                    ),
                                )
                                return 1
                            case "zero":
                                context.snap(
                                    expression,
                                    0,
                                    wording(
                                        context,
                                        "zero_power_zero_zero",
                                        "$0^0$ is configured to evaluate to $0$.",
                                        "$0^0 \\rightarrow 0$ by configuration.",
                                    ),
                                )
                                return 0
                            case _:
                                raise MathDomainError(
                                    wording(
                                        context,
                                        "zero_power_zero_undefined",
                                        "0^0 is undefined in this evaluator configuration.",
                                        "0^0 is undefined.",
                                    ),
                                    expression,
                                )
                    if preview_exponent > 0:
                        context.snap(
                            expression,
                            0,
                            wording(
                                context,
                                "zero_power_positive",
                                "0 raised to a positive power is 0.",
                                "0^n is 0 for positive n.",
                                exponent=preview_exponent,
                            ),
                        )
                        return 0
                    if preview_exponent < 0:
                        raise MathDomainError(
                            wording(
                                context,
                                "zero_power_negative",
                                "0 raised to a negative power is undefined.",
                                "0^n is undefined for negative n.",
                                exponent=preview_exponent,
                            ),
                            expression,
                        )
                symbolic_zero_power = Power(base, preview_exponent)
                context.set_status("partial", "zero_base_symbolic_exponent")
                context.snap(
                    expression,
                    symbolic_zero_power,
                    wording(
                        context,
                        "zero_power_symbolic",
                        f"Keep ${render_latex(symbolic_zero_power)}$ symbolic because the exponent's sign is unknown.",
                        "Keep 0^x symbolic when exponent sign is unknown.",
                        expression=render_latex(symbolic_zero_power),
                    ),
                )
                return symbolic_zero_power
            exponent_fraction = get_fraction(exponent)
            if exponent_fraction and exponent_fraction[0] == 1:
                new_exponent = evaluate_expression(
                    exponent,
                    EvaluatorContext(exponent),
                )  # Fake context so we don't get intermediate steps on roots.
                result = base**new_exponent
                context.snap(
                    Power(base, exponent),
                    result,
                )
                return result
            else:
                exponent = evaluate_expression(exponent, context)
            expression = Power(base, exponent)
            if base == 0 and exponent == 0:
                match context.options.zero_power_zero_policy:
                    case "one":
                        context.snap(
                            expression,
                            1,
                            wording(
                                context,
                                "zero_power_zero_one",
                                "$0^0$ is configured to evaluate to $1$.",
                                "$0^0 \\rightarrow 1$ by configuration.",
                            ),
                        )
                        return 1
                    case "zero":
                        context.snap(
                            expression,
                            0,
                            wording(
                                context,
                                "zero_power_zero_zero",
                                "$0^0$ is configured to evaluate to $0$.",
                                "$0^0 \\rightarrow 0$ by configuration.",
                            ),
                        )
                        return 0
                    case _:
                        raise MathDomainError(
                            wording(
                                context,
                                "zero_power_zero_undefined",
                                "0^0 is undefined in this evaluator configuration.",
                                "0^0 is undefined.",
                            ),
                            expression,
                        )
            if base == 1:
                result = 1
                context.snap(
                    expression,
                    result,
                    wording(
                        context,
                        "base_trivial_power",
                        "1 to any power is 1.",
                        "1 raised to any exponent is 1.",
                        base=base,
                        exponent=exponent,
                    ),
                )
                return result
            if (
                base == -1
                and is_int_or_float(exponent)
                and (
                    isinstance(exponent, int)
                    or (isinstance(exponent, float) and exponent.is_integer())
                )
            ):
                # Determine sign
                if exponent % 2 == 0:
                    result = 1
                else:
                    result = -1
                context.snap(
                    expression,
                    result,
                    wording(
                        context,
                        "minus_one_power_parity",
                        f"When $-1$ is raised to an even power, the result is $1$. When $-1$ is raised to an odd power, the result is $-1$. "
                        + (
                            f"Since in this case, our power is {exponent}, which is even, the result is $1$."
                            if exponent % 2 == 0
                            else f"Since in this case, our power is {exponent}, which is odd, the result is $-1$."
                        ),
                        f"$-1^{{{exponent}}}$ depends on parity; result is ${result}$.",
                        exponent=exponent,
                        result=result,
                    ),
                )
                return result

            if is_int_or_float(base) and is_int_or_float(exponent):
                if (
                    abs(exponent) > context.options.max_exponent
                    and abs(base) not in [0, 1]
                ):
                    if context.options.overflow_policy == "infinity":
                        context.snap(
                            expression,
                            float("inf"),
                            explanation=wording(
                                context,
                                "overflow_infinity",
                                "${previous}$ is outside the configured exponent limit, so we'll approximate it as $\\infty$.",
                                "Exponent too large; approximate as $\\infty$.",
                            ),
                            approximate=True,
                        )
                        return float("inf")
                    if context.options.overflow_policy == "zero":
                        context.snap(
                            expression,
                            0,
                            explanation=wording(
                                context,
                                "overflow_zero",
                                "${previous}$ is outside the configured exponent limit, so we'll approximate it as $0$.",
                                "Exponent too large; approximate as $0$.",
                            ),
                            approximate=True,
                        )
                        return 0
                    context.snap(
                        wording(
                            context,
                            "overflow_symbolic",
                            f"${render_latex(expression)}$ is outside the configured numeric exponent limit, so we'll keep it in symbolic form.",
                            f"Keep ${render_latex(expression)}$ symbolic due to exponent limit.",
                            expression=render_latex(expression),
                        ),
                        False,
                    )
                    return expression
                threshold = context.options.order_of_magnitude_threshold
                estimated_digits = _estimate_power_result_complexity(base, exponent)
                if (
                    threshold is not None
                    and estimated_digits is not None
                    and estimated_digits > threshold
                ):
                    exponent_int = int(exponent)
                    sign = -1 if (base < 0 and exponent_int % 2 != 0) else 1
                    approx_expr = _order_of_magnitude_expression(
                        estimated_digits - 1, sign
                    )
                    abs_base = abs(float(base))
                    log10_base = math.log10(abs_base) if abs_base > 0 else 0.0
                    scaled = exponent_int * log10_base
                    context.set_status("partial", "order_of_magnitude_estimation")
                    context.snap(
                        "Exact exponentiation is too large, so estimate using base-10 logarithms.",
                        False,
                    )
                    context.snap(
                        f"$\\log_{{10}}(|{base}^{{{exponent_int}}}|) = {exponent_int}\\cdot\\log_{{10}}(|{base}|)$.",
                        False,
                    )
                    context.snap(
                        f"$\\log_{{10}}(|{base}|) \\approx {log10_base:.6g}$, so $\\log_{{10}}(|{base}^{{{exponent_int}}}|) \\approx {scaled:.6g}$.",
                        False,
                    )
                    context.snap(
                        expression,
                        approx_expr,
                        f"So we use an order-of-magnitude estimate of ${render_latex(approx_expr)}$.",
                        approximate=True,
                    )
                    return approx_expr
                if _should_use_calculator_for_power(context, base, exponent):
                    try:
                        result = base**exponent
                    except OverflowError:
                        if context.options.overflow_policy == "infinity":
                            context.snap(
                                expression,
                                float("inf"),
                                explanation=wording(
                                    context,
                                    "overflow_python_infinity",
                                    "${previous}$ overflowed during numeric evaluation, so we'll approximate it as $\\infty$.",
                                    "Numeric overflow; approximate as $\\infty$.",
                                ),
                                approximate=True,
                            )
                            return float("inf")
                        if context.options.overflow_policy == "zero":
                            context.snap(
                                expression,
                                0,
                                explanation=wording(
                                    context,
                                    "overflow_python_zero",
                                    "${previous}$ overflowed during numeric evaluation, so we'll approximate it as $0$.",
                                    "Numeric overflow; approximate as $0$.",
                                ),
                                approximate=True,
                            )
                            return 0
                        context.snap(
                            wording(
                                context,
                                "overflow_python_symbolic",
                                f"${render_latex(expression)}$ overflowed during numeric evaluation, so we'll keep it in symbolic form.",
                                f"Keep ${render_latex(expression)}$ symbolic due to numeric overflow.",
                                expression=render_latex(expression),
                            ),
                            False,
                        )
                        return expression
                    context.snap(
                        expression,
                        result,
                        _format_calculator_message(
                            context,
                            "power",
                            expression,
                            result,
                            [base, exponent],
                        ),
                    )
                    return result
                if (
                    context.options.expand_powers
                    and exponent > 1
                    and float(exponent).is_integer()
                    and exponent
                    <= (
                        context.options.expand_power_limit
                        if context.options.expand_power_limit is not None
                        else context.options.max_precision
                    )
                ):
                    new_expression = Product(
                        [base] * math.floor(exponent)
                        + (
                            [Power(base, math.floor(exponent) % 1)]
                            if math.floor(exponent) % 1 > 0
                            else []
                        )
                    )
                    context.snap(
                        expression,
                        new_expression,
                    )
                    result = evaluate_expression(new_expression, context)
                else:
                    try:
                        result = base**exponent
                        if contains(context.current_tree, expression) > 0:
                            context.snap(
                                expression,
                                result,
                            )
                        else:
                            # Expression was normalized away in a sibling simplification.
                            # Returning the computed value keeps evaluation stable.
                            pass
                    except OverflowError:
                        if context.options.overflow_policy == "infinity":
                            context.snap(
                                expression,
                                float("inf"),
                                explanation=wording(
                                    context,
                                    "overflow_python_infinity",
                                    "${previous}$ overflowed during numeric evaluation, so we'll approximate it as $\\infty$.",
                                    "Numeric overflow; approximate as $\\infty$.",
                                ),
                                approximate=True,
                            )
                            return float("inf")
                        if context.options.overflow_policy == "zero":
                            context.snap(
                                expression,
                                0,
                                explanation=wording(
                                    context,
                                    "overflow_python_zero",
                                    "${previous}$ overflowed during numeric evaluation, so we'll approximate it as $0$.",
                                    "Numeric overflow; approximate as $0$.",
                                ),
                                approximate=True,
                            )
                            return 0
                        context.snap(
                            wording(
                                context,
                                "overflow_python_symbolic",
                                f"${render_latex(expression)}$ overflowed during numeric evaluation, so we'll keep it in symbolic form.",
                                f"Keep ${render_latex(expression)}$ symbolic due to numeric overflow.",
                                expression=render_latex(expression),
                            ),
                            False,
                        )
                        return expression
            else:
                result = power(base, exponent)
                context.snap(
                    expression,
                    result,
                )
        case Product():
            if 0 in expression.factors:
                context.snap(expression, 0)
                return 0
            factors = [
                evaluate_expression(factor, context)
                for factor in expression.factors
                if factor != 1
            ]
            current_expression = Product(factors)
            if len(factors) == 1:
                context.snap(current_expression, factors[0])
                return factors[0]
            if len(factors) == 0:
                context.snap(current_expression, 1)
                return 1
            if len(factors) != len(expression.factors):
                context.snap(expression, current_expression)
            if 0 in factors:
                context.snap(current_expression, 0)
                return 0
            # Check for a Sum to distribute
            sum_to_distribute = None
            for i, factor in enumerate(factors):
                if isinstance(factor, Sum):
                    sum_to_distribute = factor
                    # Keep track of which factor was the sum
                    sum_index = i
                    break

            if sum_to_distribute:
                other_factors = [
                    factor for i, factor in enumerate(factors) if i != sum_index
                ]
                new_terms = []
                for term in sum_to_distribute.terms:
                    # Create a new product for each term in the sum
                    new_factors = other_factors + [term]
                    new_product = product(new_factors)
                    new_terms.append(new_product)

                # The new expression is a sum of these new products
                distributed_sum = Sum(new_terms)
                context.snap(current_expression, distributed_sum)
                return evaluate_expression(distributed_sum, context)
            # Original logic if no distribution is needed
            factors = sorted(factors, key=numerical_sort_key)
            if all(is_int_or_float(factor) for factor in factors):
                with context.block(factors) as block:
                    result = block[0]
                    i = 1
                    while i < len(block):
                        factor = block[i]
                        result = multiply(result, factor, context)
                        i += 1
            else:
                new_expression = product([arg for arg in factors])
                context.snap(current_expression, new_expression)
                return new_expression
        case Sum():
            # Stage 1: Recursively evaluate all terms first.
            terms = [evaluate_expression(term, context) for term in expression.terms]
            expression = Sum(terms)

            # Stage 2: Flatten nested Sums.
            flattened_terms = []
            needs_flattening = any(isinstance(t, Sum) for t in terms)
            if needs_flattening:
                for term in terms:
                    if isinstance(term, Sum):
                        flattened_terms.extend(term.terms)
                    elif isinstance(term, Product) and len(term.factors) == 1:
                        flattened_terms.append(term.factors[0])
                    else:
                        flattened_terms.append(term)
                new_sum = Sum(flattened_terms)
                context.snap(expression, new_sum)
                expression = new_sum
                terms = flattened_terms

            # Stage 3: Combine numeric terms.
            numeric_terms = [t for t in terms if is_int_or_float(t)]
            variable_terms = [t for t in terms if not is_int_or_float(t)]
            if len(numeric_terms) > 1:
                numeric_sum = numeric_terms[0]
                with context.block(numeric_terms) as block:
                    i = 1
                    while i < len(block):
                        term = block[i]
                        numeric_sum = add(numeric_sum, term, context)
                        i += 1
                new_terms = [numeric_sum] + variable_terms
                new_sum = Sum(new_terms)
                expression = new_sum
                terms = new_terms
                numeric_terms = [numeric_sum]
            elif len(numeric_terms) == 1:
                numeric_sum = numeric_terms[0]
            if len(variable_terms) == 0 and len(numeric_terms) == 1:
                return numeric_terms[0]

            # Stage 4: Combine like variable terms.
            grouped_terms = {}
            for term in variable_terms:
                coefficient, variable_part = _get_term_parts(term)
                if variable_part not in grouped_terms:
                    grouped_terms[variable_part] = [0, variable_part]
                grouped_terms[variable_part][0] += coefficient

            reconstructed_terms = []
            for _, (coefficient, variable_part) in grouped_terms.items():
                if coefficient == 0:
                    continue
                if variable_part == 1:
                    reconstructed_terms.append(coefficient)
                elif coefficient == 1:
                    reconstructed_terms.append(variable_part)
                else:
                    reconstructed_terms.append(Product([coefficient, variable_part]))
            final_terms = numeric_terms + reconstructed_terms
            if len(final_terms) != len(terms):
                if not final_terms:
                    result = 0
                elif len(final_terms) == 1:
                    result = final_terms[0]
                else:
                    result = Sum(final_terms)
                context.snap(expression, result)
                return result
            if len(final_terms) == 1:
                result = final_terms[0]
                context.snap(expression, result)
                return result

            return expression
        case Derivative():
            bound_names = {v.name for v, _ in expression.variables}
            filtered = {
                k: v
                for k, v in context.substitutions.items()
                if not (isinstance(k, str) and k in bound_names)
            }
            inner_context = EvaluatorContext(
                expression.expression,
                filtered,
                options=context.options,
                error_on_invalid_snap=False,
            )
            inner = evaluate_expression(
                replace_symbols(expression.expression, inner_context), inner_context
            )
            derivative_expr = Derivative(inner, expression.variables)
            result_expr = inner
            for variable, order in expression.variables:
                for _ in range(order):
                    result_expr = _differentiate_once(result_expr, variable, context)
            if derivative_expr != result_expr:
                context.emit_event(
                    "derivative_simplified",
                    "derivative",
                    input_expr=expression,
                    output_expr=result_expr,
                    message="Applied native differentiation rules.",
                )
                context.snap(
                    expression,
                    result_expr,
                    wording(
                        context,
                        "derivative_result",
                        f"Differentiate with respect to "
                        + ", ".join(
                            [
                                (
                                    f"${v.name}$"
                                    if o == 1
                                    else f"${v.name}$ (order {o})"
                                )
                                for v, o in expression.variables
                            ]
                        )
                        + " using the applicable differentiation rules.",
                        "Applied differentiation rules.",
                    ),
                )
                return evaluate_expression(result_expr, context)
            context.set_status("partial", "derivative_unsolved_rule")
            return derivative_expr
        case Integral():
            filtered = {
                k: v
                for k, v in context.substitutions.items()
                if not (isinstance(k, str) and k == expression.variable.name)
            }
            inner_context = EvaluatorContext(
                expression.expression,
                filtered,
                options=context.options,
                error_on_invalid_snap=False,
            )
            inner = evaluate_expression(
                replace_symbols(expression.expression, inner_context), inner_context
            )
            lower = (
                evaluate_expression(expression.lower, context)
                if expression.lower is not None
                else None
            )
            upper = (
                evaluate_expression(expression.upper, context)
                if expression.upper is not None
                else None
            )
            current_integral = Integral(inner, expression.variable, lower, upper)
            antiderivative = _integrate_once(inner, expression.variable, context)
            if lower is None or upper is None:
                if isinstance(antiderivative, Integral):
                    context.set_status("partial", "integral_unsolved_rule")
                    return current_integral
                context.emit_event(
                    "integral_antiderivative_found",
                    "integral",
                    input_expr=expression,
                    output_expr=antiderivative,
                    message="Found antiderivative using native integration rules.",
                )
                context.snap(
                    expression,
                    antiderivative,
                    wording(
                        context,
                        "integral_indefinite_result",
                        f"Compute an antiderivative with respect to ${expression.variable.name}$.",
                        "Applied integration rules.",
                    ),
                )
                return evaluate_expression(antiderivative, context)

            if isinstance(antiderivative, Integral):
                context.set_status("partial", "definite_integral_unsolved_antiderivative")
                return current_integral

            upper_value = _substitute_symbol(antiderivative, expression.variable, upper)
            lower_value = _substitute_symbol(antiderivative, expression.variable, lower)
            difference = sum([upper_value, product([-1, lower_value])])
            context.emit_event(
                "integral_definite_evaluated",
                "integral",
                input_expr=expression,
                output_expr=difference,
                message="Applied Fundamental Theorem of Calculus with bounds.",
            )
            context.snap(
                expression,
                difference,
                wording(
                    context,
                    "integral_definite_result",
                    f"Apply the Fundamental Theorem of Calculus: evaluate the antiderivative at the bounds and subtract, $F({render_latex(upper)}) - F({render_latex(lower)})$.",
                    "Evaluate antiderivative at bounds and subtract.",
                ),
            )
            return evaluate_expression(difference, context)

        case FunctionCall():
            with context.block(
                expression.functional_arguments
            ) as functional_arguments, context.block(
                expression.subscript_arguments
            ) as subscript_arguments, context.block(
                expression.superscript_arguments
            ) as superscript_arguments:
                functional_arguments = [
                    evaluate_expression(arg, context) for arg in functional_arguments
                ]
                subscript_arguments = [
                    evaluate_expression(arg, context) for arg in subscript_arguments
                ]
                superscript_arguments = [
                    evaluate_expression(arg, context) for arg in superscript_arguments
                ]
            if (
                expression.function in context.substitutions
                and all(is_int_or_float(arg) for arg in functional_arguments)
                and all(is_int_or_float(arg) for arg in subscript_arguments)
                and all(is_int_or_float(arg) for arg in superscript_arguments)
            ):
                try:
                    result = context.substitutions[expression.function](
                        [arg for arg in functional_arguments],
                        [arg for arg in subscript_arguments],
                        [arg for arg in superscript_arguments],
                    )
                except Exception as e:  # TODO more specific.
                    raise MathDomainError(
                        str(e),
                        FunctionCall(
                            expression.function,
                            functional_arguments,
                            subscript_arguments,
                            superscript_arguments,
                        ),
                    )
            elif expression.function.name in context.substitutions and all(
                is_int_or_float(arg) for arg in functional_arguments
            ):
                try:
                    result = context.substitutions[expression.function.name](
                        [arg for arg in functional_arguments],
                        [arg for arg in subscript_arguments],
                        [arg for arg in superscript_arguments],
                    )
                except ValueError as e:
                    raise MathDomainError(
                        str(e),
                        FunctionCall(
                            expression.function,
                            functional_arguments,
                            subscript_arguments,
                            superscript_arguments,
                        ),
                    )
            else:
                result = FunctionCall(
                    expression.function,
                    [arg for arg in functional_arguments],
                    [arg for arg in subscript_arguments],
                    [arg for arg in superscript_arguments],
                )
            evaluated_call = FunctionCall(
                expression.function,
                [arg for arg in functional_arguments],
                [arg for arg in subscript_arguments],
                [arg for arg in superscript_arguments],
            )
            eval_occurrences = contains(context.current_tree, evaluated_call)
            expr_occurrences = contains(context.current_tree, expression)
            if isinstance(eval_occurrences, bool):
                eval_occurrences = int(eval_occurrences)
            if isinstance(expr_occurrences, bool):
                expr_occurrences = int(expr_occurrences)

            # Avoid globally replacing duplicate identical calls in unrelated subtrees.
            # This can corrupt nested-derivative/integral branches that should be evaluated separately.
            if eval_occurrences == 1:
                context.snap(evaluated_call, result)
            elif expr_occurrences == 1:
                context.snap(expression, result)
        case Symbol():
            if expression.name in context.substitutions:
                result = context.substitutions[expression.name]
            else:
                result = expression
    return result


def evaluate(
    expression: Numerical,
    substitutions: Optional[dict[str, int | float]] = None,
    error_on_invalid_snap: bool = True,
    options: Optional[EvaluatorOptions] = None,
):
    substitutions = substitutions or {}
    context = EvaluatorContext(
        expression,
        substitutions,
        options=options or EvaluatorOptions(),
        error_on_invalid_snap=error_on_invalid_snap,
    )
    # context.snap(f"Given the expression:\n$${render_latex(expression)}$$")
    new_expression = replace_symbols(expression, context)
    if new_expression != expression:
        variable_substitutions = {
            k: v
            for (k, v) in substitutions.items()
            if isinstance(k, str)
            and isinstance(
                v,
                (
                    int,
                    float,
                    complex,
                    Sum,
                    Product,
                    Power,
                    FunctionCall,
                    Derivative,
                    Integral,
                    Symbol,
                ),
            )
        }
        keys = list(variable_substitutions.keys())
        substitutions = []
        for k, v in variable_substitutions.items():
            substitutions.append(f"${k} = {render_latex(v)}$")
        separator_pair = context.localizer.template(
            "substitution.separator_pair", " [[substitution.separator_pair]] "
        )
        separator_many = context.localizer.template(
            "substitution.separator_many", " [[substitution.separator_many]] "
        )
        if len(substitutions) <= 1:
            substitutions_text = "".join(substitutions)
        elif len(substitutions) == 2:
            substitutions_text = separator_pair.join(substitutions)
        else:
            substitutions_text = separator_many.join(substitutions[:-1]) + separator_pair + substitutions[-1]
        context.snap(
            wording(
                context,
                "substitution_intro",
                f"Substitute the given values: {substitutions_text}.",
                f"Substitute values: {substitutions_text}.",
                substitutions=substitutions_text,
            ),
            False,
        )
        context.snap(
            expression,
            new_expression,
        )
    else:
        context.snap(expression, new_expression)
    try:
        result = evaluate_expression(new_expression, context)
        if isinstance(result, float) and result.is_integer():
            result = int(result)
    except MathDomainError as e:
        # The evaluation failed. The 'result' is the expression before the error.
        result = new_expression
        context.set_status("unsolved", "math_domain_error")
        # Add a final step explaining the domain error.
        if hasattr(e.expression, "function") and hasattr(e.expression.function, "name"):
            error_message = wording(
                context,
                "domain_error_function",
                f"Stop here: ${render_latex(e.expression)}$ is undefined for {e.expression.function.name}, so the expression is outside its domain.",
                f"${render_latex(e.expression)}$ is undefined for {e.expression.function.name}.",
                expression=render_latex(e.expression),
                function_name=e.expression.function.name,
            )
        else:
            error_message = wording(
                context,
                "domain_error_generic",
                f"Stop here: ${render_latex(e.expression)}$ is undefined in the real-number domain used by this evaluator.",
                f"${render_latex(e.expression)}$ is undefined.",
                expression=render_latex(e.expression),
            )
        context.snap(error_message)

    if _contains_node_type(result, (Integral, Derivative)):
        context.set_status("partial", "symbolic_calculus_remaining")

    return result, context
