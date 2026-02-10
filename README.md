# Expressionizer

Expressionizer is a Python library for symbolic math expression building, simplification, and step-by-step evaluation output.

It is designed for apps and tools that need explainable algebraic transformation, not just final answers. Typical use cases include math tutoring workflows, educational software, expression debugging, and generating human-readable solution traces.

## Pre-Stable Status

Expressionizer is currently in a **pre-stable (0.x)** phase.

- The core API is usable and actively developed.
- Some interfaces and behavior may change between minor versions.
- If you are using this in production, pin an exact version.

## Why Expressionizer

- Build symbolic expressions in Python.
- Evaluate with variable substitutions.
- Generate step-by-step simplification traces.
- Render expressions as plain text and LaTeX.
- Support structured expression types like equations and inequalities.
- Include procedural expression generation utilities.

## Features

- **Symbolic expression tree primitives**
  - `Symbol`, `Power`, `Product`, `Sum`, `FunctionCall`
  - `Equation` and `InEquality` data structures
- **Convenience constructors**
  - `symbol(...)`, `sum(...)`, `product(...)`, `power(...)`, `fraction(...)`
- **Expression normalization and simplification**
  - Combines numeric terms/factors
  - Merges powers and repeated structures where possible
- **Step-by-step evaluation engine**
  - `evaluate(...)` returns both the result and evaluation context
  - Context tracks snapshots and can render explanation output
  - Includes decomposition-based arithmetic steps for larger operations
- **Configurable evaluator behavior**
  - Limits and precision controls via `EvaluatorOptions`
  - Approximation and bounds behavior for very small/large numbers
- **Rendering**
  - Plain text rendering with `render(...)`
  - LaTeX rendering with `render_latex(...)`
  - Expression tree inspection with `render_type(...)`
- **Function evaluation support**
  - Works with substitutions for variables and callables
  - Includes common math function support through procedural helpers
- **Procedural generation utilities**
  - Random variable name generation
  - Random number generation with constraints
  - Weighted random expression generation for testing/content generation

## Installation

```bash
pip install expressionizer
```

## Quick Start

```python
from expressionizer import symbol, sum, product, power, evaluate, render_latex

x = symbol("x")
expr = power(sum([x, 2]), 2)

result, context = evaluate(expr, substitutions={"x": 3})

print("Result:", result)                 # 25
print("Expression (LaTeX):", render_latex(expr))
print(context.render())                  # Step-by-step output
```

## Step-by-Step Evaluation Example

```python
from expressionizer import symbol, sum, product, evaluate

x = symbol("x")
expr = product([sum([x, 4]), sum([x, -1])])

result, context = evaluate(expr, substitutions={"x": 5})

print(result)
print(context.render())
```

`context.render()` returns a formatted explanation sequence that can be displayed in apps, notebooks, or web UIs.

## Core API Overview

- `evaluate(expression, substitutions={}, error_on_invalid_snap=True)`
  - Returns `(result, context)`
- `render(expression, group=False)`
  - Plain text expression rendering
- `render_latex(expression, renderOptions=...)`
  - LaTeX rendering for display and documentation
- Constructors:
  - `symbol(name)`
  - `sum(terms)`
  - `product(factors)`
  - `power(base, exponent)`
  - `fraction(numerator, denominator)`

## Compatibility

- Python `>=3.8`
- OS independent

## Roadmap

As a pre-stable library, near-term improvements are focused on:

- API stabilization toward `1.0`
- Expanded test coverage
- Improved docs and examples
- Continued refinement of step-by-step output quality

## SEO Keywords

Python symbolic math library, step-by-step math solver, algebra expression evaluator, LaTeX math renderer, expression simplification engine, educational math software backend.

## Contributing

Issues and pull requests are welcome. If you report a bug, include:

- the expression
- substitutions used
- expected behavior
- actual behavior and rendered steps

## License

MIT
