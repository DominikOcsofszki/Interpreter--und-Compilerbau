# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class LambdaExpression(InterpretedExpression):

    def __init__(self, id, body_lambda):
        self.id=id
        self.body_lambda=body_lambda

    def eval(self,env):
        def lmbd(val):
            env_tmp = Env()
            env_tmp[self.id], env_delme = val.eval(env)
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

class LambdaArgsExpression(InterpretedExpression):

    def __init__(self, ids, body_lambda):
        self.ids=ids
        self.body_lambda=body_lambda

    def eval(self,env):
        def lmbd(vals):
            env_tmp = Env()
            for i in range(len(self.ids)):
                env_tmp[self.ids[i]], env_delme = vals[i].eval(env)
            res, env_tmp = self.body_lambda.eval(env_tmp)
            return res
        return lmbd, env

used_procedures_and_classes = getAllClasses()
