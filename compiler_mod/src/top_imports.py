from .environment import Env

from .ast.types_ast import head,tail
from .Expression import InterpretedExpression, ic
import CONFIGS
from .top_functions import print_all_test_results,test_assert

def print_py(entries:InterpretedExpression):
    for entry in entries:
        print(">>>",entry)

def show_top_env(_):
    print("TOP_ENV",environment)

def show_import_env(_):
    print("IMPORT_ENV",ENV_IMPORTS)

current_filename = ""

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
    
