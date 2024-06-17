
# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class StructExpression(InterpretedExpression):
    def __init__(self, entries):
        self.entries=entries

    def eval(self,env):
        lambda_env = Env(env.deep_copy())
        for entry in self.entries:
            tmp, lambda_env = entry.eval(lambda_env)
        def get(val):
            res,envv = val.eval(lambda_env)
            return res
        return get, env

class StructCallExpression(InterpretedExpression):
    def __init__(self, id, entry):
        self.entry=entry
        self.id=id

    def eval(self,env):
        struct, env = self.id.eval(env)
        return struct(self.entry), env

class StructExtendExpression(InterpretedExpression):
    def __init__(self,parent, entries):
        self.entries=entries
        self.parent=parent

    def eval(self,env):
        lambda_env = Env(env.deep_copy())
        for entry in self.entries:
            tmp, lambda_env = entry.eval(lambda_env)
        def get(val):
            res,envv = val.eval(lambda_env)
            return res
        return get, env

used_procedures_and_classes = getAllClasses()

