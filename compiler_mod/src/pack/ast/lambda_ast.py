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
    def __init__(self,fn,x):
        ic.enable()
        self.fn=fn
        self.x=x
        ic(fn)

    def eval(self,env):
        # fn, env = self.fn.eval(env)
        # x, env = self.x.eval(env)
        # ic(env[self.fn](self.x))
        return env[self.fn](self.x), env

class LambdaArgsExpression(InterpretedExpression):

    def __init__(self, ids, body_lambda):
        ic("=============================")
        ic(ids)
        ic(body_lambda)
        self.ids=ids
        self.body_lambda=body_lambda
    def eval(self,env):
        ic("=============================")
        def lmbd(vals):
            env_tmp = Env(env)
            ic(self.ids)
            ic(vals)
            for id, val in zip(self.ids,vals):
                ic(id)
                ic(val)
                ic(env[val])
                # env_tmp[self.ids[id]], env_delme = vals[id].eval(env)
                env_tmp[id] = val
            res, env_tmp = self.body_lambda.eval(env_tmp)
            # return res
            ic(vals[0])
            ic(vals[1])
            ic(vals[1].eval(env_tmp)[0])
            return env_tmp[vals[1].eval(env_tmp)[0]]
        return lmbd, env

used_procedures_and_classes = getAllClasses()
