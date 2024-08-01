


# from src.ast.write_read_ast import WriteIdExpression

from ..ast.write_read_ast import WriteIdExpression
from ..environment import Env
from ..Expression import InterpretedExpression, getAllClasses, ic

from ..top_configs import EVAL_EXPR_BEFORE_SAVE_TO_TMP 
from ..top_imports import ENV_IMPORTS 

        
class LambdaArgsExpression(InterpretedExpression):
    def __init__(self, ids, body_lambda):
        self.lambda_args_ids = ids
        self.body_lambda = body_lambda

    def eval(self,env):
        # ic("=============h31==================")
        lambda_env = Env(env)
        def lmbd(vals):
            ic("=============h41==================")
            ic(lambda_env)
            if vals == "self":
                ic("=============h37==================")
                ic(lambda_env)
                return lambda_env
            for i ,id_entry in enumerate(self.lambda_args_ids):
                # ic(">>>>>>>>>>>>>>>>>>>>>>>>>>>",id_entry.getWriteID())
                WriteIdExpression(id_entry.getWriteID(),vals[i]).eval(lambda_env)
            res = self.body_lambda.eval(lambda_env)[0]
            ic(lambda_env)
            ic(env)
            ic(res)
            return res
            # return self.body_lambda.eval(lambda_env)[0]
        return lmbd, env



class CallExpression(InterpretedExpression):
    def __init__(self,fn,ids_or_values):
        self.fn=fn
        self.function_args=ids_or_values

    def eval(self,env):
        ic("=============h40==================")
        ic(env)
        lmbd = env[self.fn]
        function_args = self.function_args
        if check_if_function_in_Imports(self.fn):         
            function_args=[entry.eval(env)[0] for entry in self.function_args]
        return lmbd(function_args), env


def check_if_function_in_Imports(fn):
    '''Checks for function call in Imports, iy yes unpack args first'''
    return fn in ENV_IMPORTS








used_procedures_and_classes = getAllClasses()

