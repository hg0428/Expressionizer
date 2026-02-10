import argparse
import shlex
import subprocess
import sys
from pathlib import Path


def _run(command: str, cwd: Path) -> int:
    print(f"\n[smoke] $ {command}")
    process = subprocess.run(shlex.split(command), cwd=cwd)
    return process.returncode


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Run a quick local release smoke check."
    )
    parser.add_argument(
        "--python",
        type=str,
        default=sys.executable,
        help="Python executable used for smoke commands.",
    )
    args = parser.parse_args()

    repo_root = Path(__file__).resolve().parent
    python = shlex.quote(args.python)

    commands = [
        f"{python} -m expressionizer.test",
        (
            f"{python} -m expressionizer.procedural_test --max-cases 25 --sympy-compare "
            + "--equation-mode mixed --wording-style concise --compact-explanations"
        ),
        (
            f"{python} -m expressionizer.explanation_audit --cases 25 --sympy-compare "
            + "--equation-mode mixed --wording-style concise --compact-explanations"
        ),
    ]

    for command in commands:
        if _run(command, repo_root) != 0:
            print("\n[smoke] Failed.")
            return 1
    print("\n[smoke] Passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
