from .environment import Env

from .ast.types_ast import head,tail
from .Expression import InterpretedExpression, ic

environment=Env()
def print_py(entries:InterpretedExpression):
    for entry in entries:
        print(">>>",entry)

def show_top_env(_):
    print("TOP_ENV",environment)

def show_import_env(_):
    print("IMPORT_ENV",ENV_IMPORTS)

def test_assert(arr_bool_and_msg):
    if not arr_bool_and_msg[0]: 
        raise AssertionError(*arr_bool_and_msg)
    else:
        print(f"Asserted {arr_bool_and_msg}")
    # if not arr_bool_and_msg[0]: raise AssertionError(*arr_bool_and_msg[1],arr_bool_and_msg[2])
    

ENV_IMPORTS = Env(parent=None,env_name="ENV_IMPORTS")
ENV_IMPORTS["print"]=print_py
ENV_IMPORTS["exit"]=exit
ENV_IMPORTS["_ENV"]=show_top_env
ENV_IMPORTS["_ENV_import"]=show_import_env
ENV_IMPORTS["head"]=head
ENV_IMPORTS["tail"]=tail
ENV_IMPORTS["assert"]=test_assert

environment.parent = ENV_IMPORTS

# import_names = [x for x in env_imports.env_dict]
# print(import_names)
