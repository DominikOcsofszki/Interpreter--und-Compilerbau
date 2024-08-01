

from ..environment import Env
from ..Expression import InterpretedExpression , ic
# from .tools_write_read import ReadIdExpression, WriteIdExpression

class WriteIdStructExpression(InterpretedExpression):
    def __init__(self, id_always_as_string, value):
        self.id_string=id_always_as_string
        self.value=value

    def eval(self,env):
        # find_env = findEnvWithIdWrite(self.id_string,env)
        #TODO: check for struct or other
        find_env = env
        if isinstance(self.value, str) or isinstance(self.value, int):
            find_env[self.id_string] = self.value
            return self.value, env
        else:
            find_env[self.id_string] = self.value.eval(env)[0]
            return self.value.eval(env)[0], env

class StructExpression(InterpretedExpression):
    def __init__(self, entries):
        self.entries=entries

    def eval(self,env,is_struct=True):
        struct_env = Env(env.deep_copy())
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env)
            struct_env.parent = struct_env.parent.parent
        def get(val):
            ic("=============h35==================")
            ic(val)
            if val == "self_struct":
                return struct_env
            res = struct_env[val]
            return res
        return get, env

class StructExtendExpression(InterpretedExpression):
    def __init__(self,parent, entries):
        self.entries=entries
        self.parent=parent

    def eval(self,env):
        struct_env = Env(env.deep_copy())
        new_parent_struct = env[self.parent]
        struct_env["parent_of_struct"] = new_parent_struct
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env)
        struct_env.parent = struct_env.parent.parent
        def get(val):
            ic("=============h34==================")
            ic(val)
            if val == "self_struct":
                return struct_env

            res = struct_env[val]
            return res
        return get, env


# TODO HEREHREHREHRH
class StructCallNParentFunctionExpression(InterpretedExpression):
    def __init__(self,dot_expr, fun_args):
        ic(">",self,dot_expr, fun_args)
        self.id_struct,self.dots_count, self.entry = dot_expr
        self.args_function = fun_args

    def eval(self,env,is_struct=True):
        ic(self.id_struct)
        ic(self.dots_count)
        ic(self.entry)
        parent_struct = None
        value_ret =  None
        struct_from_env = env[self.id_struct]
        if self.dots_count > 0:
            parent_struct = struct_from_env
            for _ in range(self.dots_count-1):
                parent_struct = parent_struct("parent_of_struct")
            value_ret =  parent_struct(self.entry)
            ic(value_ret)
            if self.args_function is not None:
                stru_func = value_ret
                ic(self.args_function)
                ic(stru_func(self.args_function))
                exit()
                value_ret=stru_func(self.args_function)
            return value_ret, env

# # TODO HEREHREHREHRH
# class StructNParentExpression(InterpretedExpression):
#     def __init__(self,dot_expr, fun_args):
#         # TODO Remove isncen ot usedf?
#         exit()
#         self.id_struct,self.dots_count, self.entry = dot_expr
#         self.args_function = fun_args
#
#     def eval(self,env,is_struct=True):
#         parent_struct = None
#         value_ret =  None
#         struct_from_env = env[self.id_struct]
#         if self.dots_count > 0:
#             parent_struct = struct_from_env
#             for _ in range(self.dots_count-1):
#                 parent_struct = parent_struct("parent_in_struct")
#             value_ret =  parent_struct(self.entry)
#             return value_ret, env
#         # else:
#         #     value_ret =struct_from_env(self.attribute) 
#         #     if not self.args_function == None:
#         #         fun_args = [x.eval(env)[0] for x in self.args_function]
#         #         return value_ret(fun_args),env
#         #
#         #     return value_ret,env
#         #
#         # if not value_ret:
#         #     if not parent_struct:
#         #             parent_struct = struct_from_env(self.parentString_as_readExpression)
#         #     while parent_struct and not value_ret:
#         #         value_ret = parent_struct(self.attribute)
#         #         parent_struct = parent_struct(self.parentString_as_readExpression)
#         #
#         # if not self.args_function == None:
#         #     fun_args = [x.eval(env)[0] for x in self.args_function]
#         #     return value_ret(fun_args),env
#         # return value_ret, env

