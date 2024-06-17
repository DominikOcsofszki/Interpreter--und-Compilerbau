
from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic


class CallExpression(InterpretedExpression):
    def __init__(self,fn,ids_or_values):
        self.fn=fn
        self.x=ids_or_values

    def eval(self,env):
        func = env[self.fn]
        return_ids=[entry.eval(env)[0] for entry in self.x]
        return func(return_ids), env
        
class LambdaArgsExpression(InterpretedExpression):
    def __init__(self, ids, body_lambda):
        self.ids = ids
        self.body_lambda = body_lambda

# BRAINFUCK!
    def eval(self,env):
        # lambda_env = Env(env.deep_copy())
        lambda_env = Env(env)
        def lmbd(vals):
            for i ,id_entry in enumerate(self.ids):
                lambda_env[id_entry.id] = vals[i]
            return self.body_lambda.eval(lambda_env)[0]
        return lmbd, env

used_procedures_and_classes = getAllClasses()
