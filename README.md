# Lab 1: Testing and GitHub Actions

Calculator functions (`src/calculator.py`) tested with pytest and unittest.
Two GitHub Actions workflows run the tests on every push to `main`:

- `.github/workflows/pytest_action.yml` runs pytest and uploads `pytest-report.xml` as an artifact
- `.github/workflows/unittest_action.yml` runs the unittest suite

## Run locally

    python -m venv lab_01 && source lab_01/bin/activate
    pip install -r requirements.txt
    pytest
    python -m unittest test.test_unittest
