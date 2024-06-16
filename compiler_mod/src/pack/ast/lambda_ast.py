# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic


class LambdaNoVarsExpression(InterpretedExpression):

    def __init__(self, body_lambda):
        self.body_lambda=body_lambda

    def eval(self,env):
        lambda_env = Env(env.deep_copy())
        def lmbd():
            return self.body_lambda.eval(lambda_env)[0]
        return lmbd, env

class LambdaExpression(InterpretedExpression):

    def __init__(self, id, body_lambda):
        self.id=id
        self.body_lambda=body_lambda

    def eval(self,env):
        lambda_env = Env(env.deep_copy())
        def lmbd(val):
            if len(self.id)!=0:
                lambda_env[self.id], env_delme = val[0].eval(env)
            # res, env_tmp = self.body_lambda.eval(lambda_env)
            return self.body_lambda.eval(lambda_env)[0]
            # return res
        return lmbd, env

class CallExpression(InterpretedExpression):
    def __init__(self,fn,ids_or_values):
        self.fn=fn
        self.x=ids_or_values

    def eval(self,env):
        func = env[self.fn]
        if len(self.x) != 0:
            if len(self.x) == 1:
                return env[self.fn](self.x), env
            for i in range(len(self.x)):
                self.x[i] , env = self.x[i].eval(env)
            return func(self.x), env
        return func(), env
        
class LambdaArgsExpression(InterpretedExpression):
    def __init__(self, ids, body_lambda):
        self.ids = ids
        self.body_lambda = body_lambda

    def eval(self, env):
        lambda_env = Env(env.deep_copy())
        def lmbd(vals):
            for i, id in enumerate(self.ids):
                lambda_env[id] = vals[i]
            result, env_del = self.body_lambda.eval(lambda_env)
            return result
        return lmbd, env

used_procedures_and_classes = getAllClasses()
