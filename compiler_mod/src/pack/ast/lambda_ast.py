# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic
from pack.ast.local_ast import LocalExpression

class LambdaExpression(InterpretedExpression):

    def __init__(self, id, body_lambda):
        self.id=id
        self.body_lambda=body_lambda

    def eval(self,env):
        lambda_id = self.id
        ic(lambda_id)
        lambda_body = self.body_lambda
        ic(lambda_id)
        def lmbd(val):
            env_tmp = Env()
            ic("=============================")
            ic(self.id)
            ic("=============================")
            env_tmp[self.id], env_delme = val.eval(env)
            ic(env_tmp)
            # x,env_tmp = self.id.eval(env)
            # ic(x)
            ic("=============================")
            # x,env_tmp = lambda_id.eval(env)
            ic("=============================")
            # ic(x)
            ic("=============================")
            # exit()
            # env_tmp[self.id] = val
            ic(env_tmp[self.id])
            ic(env_tmp["asd"])
            res, env_tmp = self.body_lambda.eval(env_tmp)
            return res
        return lmbd, env

class CallExpression(InterpretedExpression):
    def __init__(self,fn,x):
        self.x=x
        self.fn=fn

    def eval(self,env):
        # fn, env = self.fn.eval(env)
        # x, env = self.x.eval(env)
        return env[self.fn](self.x), env

used_procedures_and_classes = getAllClasses()
