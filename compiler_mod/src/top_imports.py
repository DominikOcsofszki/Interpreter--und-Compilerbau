from .environment import Env

from .ast.types_ast import head,tail
from .Expression import InterpretedExpression, ic
import CONFIGS
from .top_functions import print_all_test_results,test_assert
from icecream import ic

def print_py(entries:InterpretedExpression):
    for entry in entries:
        print(">>>",entry)

def _ENV():
    ic(environment.env_name,environment.env_dict)

def _ENV_import():
    ic(ENV_IMPORTS.env_name,ENV_IMPORTS.env_dict)


ENV_IMPORTS = Env(parent=None,env_name="ENV_IMPORTS")
ENV_IMPORTS["print"]=print_py
ENV_IMPORTS["exit"]=exit
ENV_IMPORTS["_ENV"]=_ENV
ENV_IMPORTS["_ENV_import"]=_ENV_import
ENV_IMPORTS["head"]=head
ENV_IMPORTS["tail"]=tail
ENV_IMPORTS["test"]=test_assert
ENV_IMPORTS["print_all_test_results"]=print_all_test_results
# ENV_IMPORTS["current_filename"]=current_filename

def setup_env_for_new_file(current_filename=''):
    global environment
    environment=Env()
    environment.env_name = "ENV_GLOBAL"
    ENV_IMPORTS["current_filename"]=current_filename

    environment.parent = ENV_IMPORTS
    return environment
    
