# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses

class LocalExpression(InterpretedExpression):
    def __init__(self, x, value, body):
        self.x=x
        self.value=value
        self.body=body

    def eval(self,env):
        local_value, old_val = self.value.eval(env)
        old_val = env[self.x]
        env[self.x] = local_value
        res, env = self.body.eval(env)
        if old_val:
            env[self.x] = old_val
        return res,env


used_procedures_and_classes = getAllClasses()

