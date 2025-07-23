#!/usr/bin/env python3
"""
Bump version for expressionizer and upload to PyPI.
Usage:
    python bump_and_upload.py <new_version>

This will:
- Update version in expressionizer/__init__.py
- Update version in pyproject.toml
- Build the package
- Upload to PyPI (will prompt for credentials)
"""
import sys
import re
import subprocess
from pathlib import Path

def update_init(version):
    init_path = Path(__file__).parent / 'expressionizer' / '__init__.py'
    text = init_path.read_text()
    new_text = re.sub(r"__version__\s*=\s*['\"]([^'\"]*)['\"]", f"__version__ = '{version}'", text)
    init_path.write_text(new_text)
    print(f"Updated __init__.py to version {version}")

def update_pyproject(version):
    pyproject_path = Path(__file__).parent / 'pyproject.toml'
    text = pyproject_path.read_text()
    new_text = re.sub(r"version\s*=\s*['\"]([^'\"]*)['\"]", f"version = '{version}'", text)
    pyproject_path.write_text(new_text)
    print(f"Updated pyproject.toml to version {version}")

def build_package():
    print("Cleaning old build artifacts...")
    import shutil
    for path in ["build", "dist", "expressionizer.egg-info"]:
        shutil.rmtree(path, ignore_errors=True)
    print("Building package...")
    subprocess.run([sys.executable, '-m', 'build'], check=True)

def upload_package():
    print("Uploading to PyPI...")
    subprocess.run([sys.executable, '-m', 'twine', 'upload', 'dist/*'])

def main():
    if len(sys.argv) != 2:
        print("Usage: python bump_and_upload.py <new_version>")
        sys.exit(1)
    version = sys.argv[1]
    update_init(version)
    update_pyproject(version)
    build_package()
    upload_package()

if __name__ == "__main__":
    main()
