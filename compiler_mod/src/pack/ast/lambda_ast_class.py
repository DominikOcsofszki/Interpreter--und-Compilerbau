# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses

class LambdaExpression(InterpretedExpression):
    def __init__(self, x, body):
        self.x=x
        self.body=body

    def eval(self,env):

        def lmbd(val):
            lambda_env = Env(env)
            lambda_env[self.x]=val
            res, env_tmp = self.body.eval(lambda_env)
            return res
        return lmbd, env

used_procedures_and_classes = getAllClasses()

