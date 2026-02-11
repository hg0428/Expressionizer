# Changelog

All notable changes are documented in this file.

## 0.8.0 (planned)

### Added

- Native equation solving with step-by-step explanations:
  - single-variable linear equations
  - quadratic equations (real roots)
  - simple rational equations with domain checks
  - linear systems via elimination
- Equation generation utilities for procedural testing/manual review.
- Calculator mode for long numeric arithmetic:
  - configurable thresholds by operation
  - customizable templates for explanation text
  - operation-specific template overrides for AI training-data workflows
- Generation profile control (`realistic` / `stress`) for expression generation.
- Dedicated equation manual-review generator and release smoke/checklist utilities.

### Improved

- Explanation clarity and mathematical rigor:
  - operation-explicit equation steps
  - exact-first numeric presentation with optional approximations
  - matrix state snapshots for system-solving steps
- Sign rendering normalization to avoid `+ -` artifacts in user-visible explanations.
- Robustness under long procedural runs with improved explanation auditing.

### Fixed

- Multiple explanation and rendering edge cases (including snapshot integrity and formatting issues).
- Numeric/rendering overflow and large-number formatting edge cases.
- SymPy comparison mapping mismatches for selected native functions.
