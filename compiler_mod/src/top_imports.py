from environment import Env

# my functions:
from pack.ast.types_ast import head,tail
from pack.ast.Expression import InterpretedExpression, ic

env={}
def print_py(entry:InterpretedExpression):
    # if entry is InterpretedExpression:
    #     print("entry if: ")
    #     print(entry)
    # entry = entry[0].eval(env)
    print(">>>",entry)
    # ic(entry[0].eval(env)[0])

env_imports = Env()
env_imports["print"]=print_py
env_imports["head"]=head
env_imports["tail"]=tail


