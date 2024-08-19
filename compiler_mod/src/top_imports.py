import enum

from icecream import ic

import CONFIGS

from .ast.types_ast import head, tail
from .environment import Env
from .Expression import InterpretedExpression
from .symbol_table import SYMBOL_TABLE
from .top_tests_fun import print_all_test_results, test_assert, test_false


def print_py(entries: InterpretedExpression):
    if not CONFIGS.DEACTIVATE_PRINT:
        for entry in entries:
            print(">>>", entry)


def _ENV():
    ic(environment.env_name, environment.env_dict)


def _ENV_import():
    ic(ENV_IMPORTS.env_name, ENV_IMPORTS.env_dict)


class Test_enum(enum.Enum):
    test = "test"
    test_not_eq = "test_false"
    print_all_tests = "print_all_tests"


def print_SYMBOL_TABLE():
    ic(">>>>", SYMBOL_TABLE)


ENV_IMPORTS = Env(parent=None, env_name="ENV_IMPORTS")
ENV_IMPORTS["print"] = print_py
ENV_IMPORTS["exit"] = exit
ENV_IMPORTS["_ENV"] = _ENV
ENV_IMPORTS["_ENV_IMPORT"] = _ENV_import
ENV_IMPORTS["head"] = head
ENV_IMPORTS["tail"] = tail
ENV_IMPORTS["test"] = test_assert
ENV_IMPORTS[Test_enum.test.value] = test_assert
ENV_IMPORTS[Test_enum.test_not_eq.value] = test_false
ENV_IMPORTS[Test_enum.print_all_tests.value] = print_all_test_results
# ENV_IMPORTS["current_filename"]=current_filename


def setup_env_for_new_file(current_filename=""):
    ENV_IMPORTS["SYMBOL_TABLE"] = print_SYMBOL_TABLE
    global environment
    ENV_IMPORTS["current_filename"] = current_filename
    environment = Env(parent=ENV_IMPORTS, env_name="ENV_GLOBAL")
    # environment.env_name = "ENV_GLOBAL"

    # environment.parent = ENV_IMPORTS
    # SYMBOL_TABLE.add_global_var("_EXTERNAL", ENV_IMPORTS)

    return environment
