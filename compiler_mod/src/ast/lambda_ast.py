


# from src.ast.write_read_ast import WriteIdExpression

from ..ast.write_read_ast import WriteIdExpression
from ..environment import Env
from ..Expression import InterpretedExpression, getAllClasses, ic

from ..top_configs import EVAL_EXPR_BEFORE_SAVE_TO_TMP 
from ..top_imports import ENV_IMPORTS, Test_enum

        
class LambdaArgsExpression(InterpretedExpression):
    def __init__(self, ids, body_lambda):
        self.lambda_args_ids = ids
        self.body_lambda = body_lambda

    def eval(self,env,is_struct=False):
        ic(env)
        ic(len(env.struct_dict))
        ls = len(env.struct_dict)
        if ls > 0:
            exit()

        lambda_env = Env(env)
        def lmbd(vals):
            for i ,id_entry in enumerate(self.lambda_args_ids):
                # ic(">>>>>>>>>>>>>>>>>>>>>>>>>>>",id_entry.getWriteID())
                WriteIdExpression(id_entry.getWriteID(),vals[i]).eval(lambda_env,is_struct)
            return self.body_lambda.eval(lambda_env)[0]
        return lmbd, env



#H_Call
class CallExpression(InterpretedExpression):
    def __init__(self,fn,ids_or_values):
        self.fn=fn
        self.ids_or_values=ids_or_values

    def eval(self,env,is_struct=False):
        func = env[self.fn]
        if func is None:
            raise RuntimeError(f"[CallExpression] Function: {self.fn} not found")
        if self.fn in ENV_IMPORTS:
            ic("=============h10==================")
            ic(self.fn)
            ic(self.ids_or_values)
            if Test_enum.test.value == self.fn or Test_enum.test_not_eq.value  == self.fn :
                return_ids=[entry.eval(env)[0] for entry in self.ids_or_values]
                return func(return_ids,env), env
            return_ids=[entry.eval(env)[0] for entry in self.ids_or_values]
            if len(return_ids) == 0:
                return func(),env
            return func(return_ids), env

        # if not EVAL_EXPR_BEFORE_SAVE_TO_TMP:
        #     return_ids=[entry.eval(env)[0] for entry in self.ids_or_values]
        #     return func(return_ids), env

        # if EVAL_EXPR_BEFORE_SAVE_TO_TMP:
        ic("=============h9==================")
        return func(self.ids_or_values), env










used_procedures_and_classes = getAllClasses()

