from __future__ import annotations

import argparse
import ast
import json
import re
from pathlib import Path
from typing import Any

from .language_packs import (
    get_builtin_messages,
    locale_equal_to_english_keys,
    supported_locales,
    validate_pack_placeholders,
)


def _literal_string(node: ast.AST | None) -> str | None:
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    if isinstance(node, ast.JoinedStr):
        parts: list[str] = []
        for value in node.values:
            if isinstance(value, ast.Constant) and isinstance(value.value, str):
                parts.append(value.value)
                continue
            if isinstance(value, ast.FormattedValue):
                inner = value.value
                if isinstance(inner, ast.Name):
                    parts.append("{" + inner.id + "}")
                    continue
                if isinstance(inner, ast.Attribute):
                    parts.append("{" + inner.attr + "}")
                    continue
                parts.append("{value}")
                continue
            return None
        return "".join(parts)
    return None


def _extract_keys_from_file(path: Path) -> dict[str, str | None]:
    source = path.read_text(encoding="utf-8")
    tree = ast.parse(source, filename=str(path))
    keys: dict[str, str | None] = {}

    for node in ast.walk(tree):
        if not isinstance(node, ast.Call):
            continue

        # wording(context, "key", "default", ...)
        if isinstance(node.func, ast.Name) and node.func.id == "wording":
            if len(node.args) >= 2:
                key = _literal_string(node.args[1])
                if key is not None:
                    default = _literal_string(node.args[2]) if len(node.args) >= 3 else None
                    keys.setdefault(key, default)
            continue

        # _msg(context, "key", "default", ...)
        if isinstance(node.func, ast.Name) and node.func.id == "_msg":
            if len(node.args) >= 2:
                key = _literal_string(node.args[1])
                if key is not None:
                    default = _literal_string(node.args[2]) if len(node.args) >= 3 else None
                    keys.setdefault(key, default)
            continue

        # localizer.template("key", "default")
        # localizer.format("key", "default", payload)
        if isinstance(node.func, ast.Attribute) and node.func.attr in ("template", "format"):
            if len(node.args) >= 1:
                key = _literal_string(node.args[0])
                if key is not None:
                    default = _literal_string(node.args[1]) if len(node.args) >= 2 else None
                    keys.setdefault(key, default)

    return keys


def collect_catalog() -> dict[str, Any]:
    repo_root = Path(__file__).resolve().parents[1]
    targets = [
        repo_root / "expressionizer" / "evaluator.py",
        repo_root / "expressionizer" / "solve_equation.py",
        repo_root / "expressionizer" / "manual_review_cases.py",
        repo_root / "expressionizer" / "equation_manual_review_cases.py",
    ]
    combined: dict[str, str | None] = {}
    for path in targets:
        for key, default in _extract_keys_from_file(path).items():
            combined.setdefault(key, default)

    placeholder_pattern = re.compile(r"\{([a-zA-Z_][a-zA-Z0-9_]*)\}")
    entries = []
    for key in sorted(combined):
        default = combined[key]
        placeholders = sorted(set(placeholder_pattern.findall(default))) if default else []
        entries.append(
            {
                "key": key,
                "default_template": default,
                "placeholders": placeholders,
            }
        )
    return {"keys": entries, "total_keys": len(entries)}


def validate_locale_packs() -> list[str]:
    errors: list[str] = []
    catalog = collect_catalog()
    catalog_defaults = {entry["key"]: entry.get("default_template") for entry in catalog["keys"]}
    for locale in supported_locales():
        errors.extend(validate_pack_placeholders(locale))
        merged = get_builtin_messages(locale, "default")
        missing_runtime = [
            key
            for key, default in catalog_defaults.items()
            if key not in merged and default is None
        ]
        if missing_runtime:
            errors.append(
                f"{locale}: keys lack both built-in value and literal code default: {', '.join(sorted(missing_runtime))}"
            )
    return errors


def locale_coverage_report() -> dict[str, Any]:
    catalog = collect_catalog()
    catalog_keys = [entry["key"] for entry in catalog["keys"]]
    total = len(catalog_keys)
    report: dict[str, Any] = {"total_keys": total, "locales": {}}
    for locale in supported_locales():
        untranslated = locale_equal_to_english_keys(locale)
        translated = total - len(untranslated)
        report["locales"][locale] = {
            "translated_or_customized_keys": translated,
            "untranslated_keys": len(untranslated),
            "coverage_ratio": 0.0 if total == 0 else round(translated / total, 4),
        }
    return report


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Generate and validate localization key catalog."
    )
    parser.add_argument(
        "--output",
        type=str,
        default="localization_keys.json",
        help="Output JSON path (repo-relative or absolute).",
    )
    parser.add_argument(
        "--validate-only",
        action="store_true",
        default=False,
        help="Validate locale packs without writing catalog file.",
    )
    parser.add_argument(
        "--print-coverage",
        action="store_true",
        default=False,
        help="Print locale coverage report derived from catalog keys.",
    )
    parser.add_argument(
        "--require-full-locale-coverage",
        action="store_true",
        default=False,
        help="Fail validation if non-English locales still match English for any tracked key.",
    )
    args = parser.parse_args()

    errors = validate_locale_packs()
    coverage = locale_coverage_report()
    if args.require_full_locale_coverage:
        for locale, row in coverage["locales"].items():
            if locale == "en":
                continue
            if row["untranslated_keys"] > 0:
                errors.append(
                    f"{locale}: untranslated key count {row['untranslated_keys']} (require-full-locale-coverage enabled)"
                )
    if errors:
        print("Localization validation errors:")
        for error in errors:
            print(f"- {error}")
        return 1

    if args.print_coverage:
        print(json.dumps(coverage, indent=2, sort_keys=True, ensure_ascii=False))

    if args.validate_only:
        print("Localization validation passed.")
        return 0

    catalog = collect_catalog()
    output = Path(args.output)
    if not output.is_absolute():
        output = Path(__file__).resolve().parents[1] / output
    output.write_text(json.dumps(catalog, indent=2, ensure_ascii=False), encoding="utf-8")
    print(f"Wrote {catalog['total_keys']} localization keys to {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
