

from ..environment import Env
from ..Expression import InterpretedExpression , ic
from .tools_write_read import ReadIdExpression, WriteIdExpression
# from ..Expr_Enum import Expr
# from ..Nodes import Node

class StructExpression(InterpretedExpression):
    def __init__(self, entries):
        # ic(self, entries)
        self.entries=entries

    def eval(self,env,is_struct=True):
        lambda_env = Env(env.deep_copy())
        for entry in self.entries:
            tmp, lambda_env = entry.eval(lambda_env)
            lambda_env.parent = lambda_env.parent.parent
        def get(val):
            res = lambda_env[val]
            return res
        return get, env

class StructExtendExpression(InterpretedExpression):
    def __init__(self,parent, entries):
        self.entries=entries
        self.parent=parent

    def eval(self,env):
        struct_env = Env(env.deep_copy())
        new_parent_struct = env[self.parent]
        struct_env["parent_in_struct"] = new_parent_struct
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env)
        def get(val):
            res = struct_env[val]
            return res
        return get, env

# TODO HEREHREHREHRH
class StructCallNParentWithFunExpression(InterpretedExpression):
    def __init__(self,dot_expr, fun_args):
        # ic("=============h19==================")
        # ic(self,dot_expr, fun_args)
        self.id_struct,self.dots_count, self.entry = dot_expr
        self.args_function = fun_args

    def eval(self,env,is_struct=True):
        # ic("=============h23==================")
        # if len(self.id_struct) == 0:
        #     if self.dots_count ==2:
        #         ic(self.id_struct,self.entry,self.dots_count)
        #         # ic(env.parent[self.parentString_as_readExpression.eval(env)[1]])
        #         # ic(env.parent[self.parentString_as_readExpression.eval(env)[1]])
        #     #TODO>>>>???
        #     exit()

        parent_struct = None
        value_ret =  None
        struct_from_env = env[self.id_struct]
        # ic(struct_from_env)
        if self.dots_count > 0:
            # ic(self.dots_count)
            # parent_struct = struct_from_env("parent_in_struct")
            parent_struct = struct_from_env
            for _ in range(self.dots_count-1):
                parent_struct = parent_struct("parent_in_struct")
            # ic(self.entry)
            value_ret =  parent_struct(self.entry)
            # ic(value_ret)
            return value_ret, env
        # else:
        #     value_ret =struct_from_env(self.attribute) 
        #     if not self.args_function == None:
        #         fun_args = [x.eval(env)[0] for x in self.args_function]
        #         return value_ret(fun_args),env
        #
        #     return value_ret,env
        #
        # if not value_ret:
        #     if not parent_struct:
        #             parent_struct = struct_from_env(self.parentString_as_readExpression)
        #     while parent_struct and not value_ret:
        #         value_ret = parent_struct(self.attribute)
        #         parent_struct = parent_struct(self.parentString_as_readExpression)
        #
        # if not self.args_function == None:
        #     fun_args = [x.eval(env)[0] for x in self.args_function]
        #     return value_ret(fun_args),env
        # return value_ret, env

