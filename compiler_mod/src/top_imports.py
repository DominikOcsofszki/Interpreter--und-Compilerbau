from .environment import Env

from .ast.types_ast import head,tail
from .Expression import InterpretedExpression, ic

def print_py(entries:InterpretedExpression):
    for entry in entries:
        print(">>>",entry)

def show_top_env(_):
    print("TOP_ENV",environment)

def show_import_env(_):
    print("IMPORT_ENV",ENV_IMPORTS)

passed_tests = []
failed_tests = []

def padding(txt):
    padding = 20 - len(txt)
    return "_" * padding


def print_all_test_results():
    ic("TODO: get info from Node, atm only latest")
    # ic(passed_tests)
    # ic(failed_tests)
    print("\033[92mPassed Tests:\033[0m")  # Green

    for test in passed_tests:
        if "IMPORTANT" in test[2]:
            print(f"\033[92m-> {test[2]!r}{padding(test[2])} {test[:-1]}\033[0m")

        else:
            print(f"|- {test[2]!r}{padding(test[2])} {test[:-1]}")
    print("\033[91mFailed Tests:\033[0m")  # Red
    for test in failed_tests:
        if "IMPORTANT" in test[2]:
            print(f"\033[91m-> {test[2]!r}{padding(test[2])} {test[:-1]}\033[0m")
        else:
            print(f"|- {test[2]!r}{padding(test[2])} {test[:-1]}")

    print("================END-TESTS===================")

def test_assert(arr_bool_and_msg, my_helper):
    msg = *arr_bool_and_msg, my_helper['tok']
    test_bool = arr_bool_and_msg[0] == arr_bool_and_msg[1]
    if not test_bool: 
        failed_tests.append(msg)
    else:
        passed_tests.append(msg)
    
current_filename = ""

# import_names = [x for x in env_imports.env_dict]
# print(import_names)

ENV_IMPORTS = Env(parent=None,env_name="ENV_IMPORTS")
ENV_IMPORTS["print"]=print_py
ENV_IMPORTS["exit"]=exit
ENV_IMPORTS["_ENV"]=show_top_env
ENV_IMPORTS["_ENV_import"]=show_import_env
ENV_IMPORTS["head"]=head
ENV_IMPORTS["tail"]=tail
ENV_IMPORTS["test"]=test_assert
ENV_IMPORTS["print_all_test_results"]=print_all_test_results
ENV_IMPORTS["current_filename"]=current_filename
def setup_env_for_new_file():
    global environment
    environment=Env()

    environment.parent = ENV_IMPORTS
    return environment
    
# environment,ENV_IMPORTS=setup_env_for_new_file()
# setup_env_for_new_file()
