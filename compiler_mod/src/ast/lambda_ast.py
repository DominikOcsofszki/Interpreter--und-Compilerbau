


# from src.ast.write_read_ast import WriteIdExpression

from ..environment import Env
from ..Expression import InterpretedExpression, getAllClasses, ic

from ..top_configs import EVAL_EXPR_BEFORE_SAVE_TO_TMP 
from ..top_imports import ENV_IMPORTS 

        
class LambdaArgsExpression(InterpretedExpression):
    def __init__(self, ids, body_lambda):
        self.ids = ids
        self.body_lambda = body_lambda

    def eval(self,env):
        lambda_env = Env(env)
        def lmbd(vals):
            ic(self.ids)
            # self.ids = [self.ids]
            for i ,id_entry in enumerate(self.ids):
                # ic(vals[i])
                # ic(id_entry.getEntries())
                # ic(id_entry.eval(env))
                # lambda_env[id_entry.id] = vals[i]
                lambda_env[id_entry.getLiteral()] = vals[i]
            return self.body_lambda.eval(lambda_env)[0]
        return lmbd, env



class CallExpression(InterpretedExpression):
    def __init__(self,fn,ids_or_values):
        ic(self,fn,ids_or_values)
        self.fn=fn
        self.x=ids_or_values

    def eval(self,env):
        func = env[self.fn]
        if self.fn in ENV_IMPORTS:
            return_ids=[entry.eval(env)[0] for entry in self.x]
            return func(return_ids), env

        if not EVAL_EXPR_BEFORE_SAVE_TO_TMP:
            return_ids=[entry.eval(env)[0] for entry in self.x]
            return func(return_ids), env

        # if EVAL_EXPR_BEFORE_SAVE_TO_TMP:
        return func(self.x), env










used_procedures_and_classes = getAllClasses()

