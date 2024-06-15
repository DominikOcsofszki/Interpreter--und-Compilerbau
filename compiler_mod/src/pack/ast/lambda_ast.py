# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic


class LambdaExpression(InterpretedExpression):

    def __init__(self, id, body_lambda):
        self.id=id
        self.body_lambda=body_lambda

    def eval(self,env):
        def lmbd(val):
            env_tmp = Env(env)
            env_tmp[self.id], env_delme = val[0].eval(env)
            res, env_tmp = self.body_lambda.eval(env_tmp)
            return res
        return lmbd, env

class CallExpression(InterpretedExpression):
    def __init__(self,fn,ids_or_values):
        self.fn=fn
        self.x=ids_or_values

    def eval(self,env):
        if len(self.x) == 1:
            return env[self.fn](self.x), env
        for i in range(len(self.x)):
            self.x[i] , env = self.x[i].eval(env)
        func = env[self.fn]
        return func(self.x)

        ic("=============================")
        
class LambdaArgsExpression(InterpretedExpression):
    def __init__(self, ids, body_lambda):
        self.ids = ids
        self.body_lambda = body_lambda

    def eval(self, env):
        def lmbd(vals):
            env_closure = Env(env)
            for i, id in enumerate(self.ids):
                env_closure[id] = vals[i]
            result, env_del = self.body_lambda.eval(env_closure)
            return result
        return lmbd, env

class LambdaArgsExpression2(InterpretedExpression):

    def __init__(self, ids, body_lambda):
        self.ids=ids
        self.body_lambda=body_lambda
    def eval(self,env):
        def lmbd(vals):
            env_closure = Env(env)
            ic(env_closure)
            for i in range(len(vals)):
                ic(self.ids[i].eval(env_closure))
                env_closure[self.ids[i].eval(env_closure)[0]] = vals[i]
                ic(env_closure)
            result, env_del = self.body_lambda.eval(env_closure)
            return result

        # def lmbd(val):
        #     env_tmp = Env(env)
        #     for id in range(self.ids):
        #         env_tmp[id], env_delme = val[0].eval(env)
        #     env_tmp[self.id], env_delme = val[0].eval(env)
        #     res, env_tmp = self.body_lambda.eval(env_tmp)
        #     return res
        # def lmbd(vals):
        #     env_tmp = Env(env)
        #     ic(vals)
        #     for id, val in zip(self.ids,vals):
        #         # env_tmp[self.ids[id]], env_delme = vals[id].eval(env)
        #         env_tmp[id] = val
        #     res, env_tmp = self.body_lambda.eval(env_tmp)
        #     # return res
        #     return env_tmp[vals[1].eval(env_tmp)[0]]
        return lmbd, env

used_procedures_and_classes = getAllClasses()
