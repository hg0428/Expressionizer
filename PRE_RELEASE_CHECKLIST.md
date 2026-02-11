# Pre-Release Checklist

Use this checklist before tagging/publishing a stable release.

## 1) Code + Tests

- Run full suite:
  - `python -m expressionizer.test`
- Compatibility smoke (if interpreters are available):
  - `python3.10 -m expressionizer.test`
  - `python3.11 -m expressionizer.test`
  - `python3.12 -m expressionizer.test`
- Run smoke script:
  - `python release_smoke.py`
- Run longer procedural soak (realistic profile):
  - `python -m expressionizer.procedural_test --max-cases 500 --sympy-compare --equation-mode mixed --generation-profile realistic --wording-style concise --compact-explanations --report-every 100`
- Run longer explanation audit (realistic profile):
  - `python -m expressionizer.explanation_audit --cases 500 --sympy-compare --equation-mode mixed --generation-profile realistic --wording-style concise --compact-explanations --report-every 100`

## 2) Explanation Quality

- Generate fresh manual review set:
  - `python -m expressionizer.manual_review_cases --cases 60 --generation-profile realistic --output manual_review_cases_release.md`
- Generate fresh equation review set:
  - `python -m expressionizer.equation_manual_review_cases --cases 60 --output equation_manual_review_cases_release.md`
- Verify:
  - no runaway/overly long arithmetic traces for normal user-facing cases
  - explanations have no `+ -` artifacts
  - equations show operation-explicit steps and matrix states for systems

## 3) Packaging + Metadata

- Confirm package metadata and docs are current:
  - `pyproject.toml`
  - `expressionizer/__init__.py`
  - `README.md`
- Build artifacts:
  - `python -m build`
- Validate wheel/sdist contents:
  - ensure source files are present
  - ensure transient files (`__pycache__`, temp files) are excluded

## 4) Final Sanity

- Confirm `git status` only includes intended files.
- Re-run one final smoke pass after any last-minute edits.
- Tag/publish only after all checks above pass.
