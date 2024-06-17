# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class LocalExpression(InterpretedExpression):
    def __init__(self, assign_to_id, value, body):
        self.assign_to_id=assign_to_id
        self.value=value
        self.body=body

    def eval(self,env):
        local_value, old_val = self.value.eval(env)
        old_val = env[self.assign_to_id]
        env[self.assign_to_id] = local_value
        res, env = self.body.eval(env)
        if old_val:
            env[self.assign_to_id] = old_val
        return res,env


used_procedures_and_classes = getAllClasses()

