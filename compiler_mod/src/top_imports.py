from environment import Env

from pack.ast.types_ast import head,tail
from pack.ast.Expression import InterpretedExpression, ic

environment=Env()
def print_py(entries:InterpretedExpression):
    for entry in entries:
        print(">>>",entry)

def show_top_env(_):
    print("TOP_ENV",environment)

def show_import_env(_):
    print("IMPORT_ENV",ENV_IMPORTS)

ENV_IMPORTS = Env(parent=None,env_name="ENV_IMPORTS")
ENV_IMPORTS["print"]=print_py
ENV_IMPORTS["_ENV"]=show_top_env
ENV_IMPORTS["_ENV_import"]=show_import_env
ENV_IMPORTS["head"]=head
ENV_IMPORTS["tail"]=tail

environment.parent = ENV_IMPORTS

# import_names = [x for x in env_imports.env_dict]
# print(import_names)
