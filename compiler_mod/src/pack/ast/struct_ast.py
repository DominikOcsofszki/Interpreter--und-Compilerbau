
# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class StructExpression(InterpretedExpression):
    def __init__(self, entries):
        self.entries=entries

    def eval(self,env):
        lambda_env = Env(env.deep_copy())
        ic(self.entries)
        for entry in self.entries:
            ic(entry)
            tmp, lambda_env = entry.eval(lambda_env)
        def lmbd(vals):
            for val in vals:
                res,envv = val.eval(env)
            return res
        return lmbd, env

class StructCallExpression(InterpretedExpression):
    def __init__(self, id, entry):
        ic(self, id, entry)
        self.entry=entry
        self.id=id

    def eval(self,env):
        name, _env = self.id.eval(env)

used_procedures_and_classes = getAllClasses()

