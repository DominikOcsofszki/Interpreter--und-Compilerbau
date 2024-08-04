# Interpreter--und-Compilerbau

# Work Folder:
compiler_mod

# CONFIGS
CONFIGS.py contains the configuration settings. 
## RUN_TESTS_ONLY=True
- if True run the whole tests found in: 'compiler_mod/code/tests/all_tests.tx'
- if False run the first (not starting with #) file in 'compiler_mod/code.tx'

## PRINT_LEXER_TOK_LINE_AND_NR=False
- show line and token nr, new token_nr per line
## PRINT_ALL_TOEKNS_LITERALS_AT_START=False
## SHOW_ENV_IMPORTS=False
## SHOW_ENV_AFTER_TEST_RUN=False
## COLORIZE=True
- if issues with terminal(eg:\033[91m), removes the color for Tests 
## DEACTIVATE_PRINT=False
- deactivate print statements inside incc-language

## HELP_PRINTS=True
- print additional info for debugging


# code/
This directory holds code files.
- run from code.tx 

# code/tests/
This subdirectory contains additional test files for the project.
- run from code/tests/all_tests.tx

# requirements.txt
Python package dependencies required for the project

# Getting Started
Create a new virtual environment and activate it.
Install the project dependencies by running `pip install -r requirements.txt`.
Run the project using the RUN.py file.


# RUN.py
```sh
cd compiler_mod/
python3 RUN.py

```
for Development:
```sh
cd compiler_mod/
watchexec python3 run.py
```
- watchexec watches for file changes and run the run.py
- helpful for continuous feedback
- (brew install watchexec)


# TODO

## Known issues:
- line not reseting if multiple files

