# Readme

## File strucutre

- `/src/gui/` Contains code related to the software GUI.
- `/src/state/` Contaions code related to state management system.
- `/src/tests/` Contains testing code and test files.
- `/src/data_processing/` Contains code related to the analysis pipeline including analysis calculations and file creation.
- Additionally, `/src/output` and `/src/saved_runs` are used to store persistent data and may or may not exist depending on when the software is run.

## Build instructions

### Requirements

- Python 3.7
- Packages: listed in `requirements.txt`
- Tested on Windows 10

#### To Compile Locally

- `pip install pyinstaller`
- `cd src`
- `pyinstaller -D main.spec`
- Compiled directory found at `/dist/main`. Run via `main.exe`.

### Test steps

- `cd src`
- `python -m unittest discover -p test_unit*`
