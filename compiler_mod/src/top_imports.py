from environment import Env

# my functions:
from pack.ast.types_ast import head,tail
from pack.ast.Expression import InterpretedExpression, ic

environment=Env()
def print_py(entries:InterpretedExpression):
    # ic(entries)
    for entry in entries:
        print(">>>",entry)
        # print(">>>",entry.eval(environment)[0])
        # x.eval(env)
    # if entry is InterpretedExpression:
    #     print("entry if: ")
    #     print(entry)
    # entry = entry[0].eval(env)
    # print(">>>",entries.eval(env))
    # ic(entry[0].eval(env)[0])

env_imports = Env()
env_imports["print"]=print_py
env_imports["head"]=head
env_imports["tail"]=tail

environment.parent = env_imports
