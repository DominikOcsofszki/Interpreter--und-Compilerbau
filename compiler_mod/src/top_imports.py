from environment import Env

from pack.ast.types_ast import head,tail
from pack.ast.Expression import InterpretedExpression, ic

environment=Env()
def print_py(entries:InterpretedExpression):
    for entry in entries:
        print(">>>",entry)

env_imports = Env()
env_imports["print"]=print_py
env_imports["head"]=head
env_imports["tail"]=tail

environment.parent = env_imports
