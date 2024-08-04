
from dataclasses import dataclass
from typing import List

from ..environment import Env
from ..Expression import InterpretedExpression , ic
# from .tools_write_read import ReadIdExpression, WriteIdExpression

# class StructExpression(InterpretedExpression):
#     def __init__(self, entries):
#         self.entries=entries
#
#     def eval(self,env,is_struct=True):
#         lambda_env = Env(env.deep_copy())
#         for entry in self.entries:
#             tmp, lambda_env = entry.eval(lambda_env)
#             lambda_env.parent = lambda_env.parent.parent
#         def get(val):
#             res = lambda_env[val]
#             return res
#         return get, env
@dataclass
class StructExpression(InterpretedExpression):
    entries: List
    def eval(self,env:Env):
        struct_env = Env(env)
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env)
        struct_env.struct_dict = struct_env.deep_copy__only_env()
        struct_env.struct_dict["struct_parent"] = None 
        struct_env.struct_dict["struct_env"] = struct_env.struct_dict
        def struct_get(val):
            # res = struct_env.struct_dict[val]
            res = struct_env.struct_dict.get(val,None)
            return res
            # lambda_env.parent = lambda_env.parent.parent
        return struct_get, env

@dataclass
class StructExtendExpression(InterpretedExpression):
    parent: InterpretedExpression
    entries: List
    def eval(self,env:Env):
        struct_env = Env(env)
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env)
            # _, _ = entry.eval(struct_env)
        struct_env.struct_dict = struct_env.deep_copy__only_env()
        struct_env.struct_dict["struct_parent"] = env[self.parent]
        struct_env.struct_dict["struct_env"] = struct_env.struct_dict
        def struct_get(val):
            # res = struct_env.struct_dict[val]
            res = struct_env.struct_dict.get(val,None)
            return res
        return struct_get, env

# class StructExtendExpression(InterpretedExpression):
#     def __init__(self,parent, entries):
#         self.entries=entries
#         self.parent=parent
#
#     def eval(self,env):
#         struct_env = Env(env.deep_copy())
#         new_parent_struct = env[self.parent]
#         struct_env["parent_in_struct"] = new_parent_struct
#         for entry in self.entries:
#             tmp, struct_env = entry.eval(struct_env)
#         def get(val):
#             res = struct_env[val]
#             return res
#         return get, env

class StructInsideArgsExpression(InterpretedExpression):
    def __init__(self,dot_expr, fun_args):
        self.id_struct,self.dots_count, self.entry = dot_expr
        self.args_function = fun_args
        exit()

def get_struct_x_parent_or_self_struct(struct_get,dots_count):
    struct = struct_get
    parent_up = dots_count - 1
    for _ in range(parent_up):
        _struct = get_struct_parent(struct)
        if _struct is None:
            raise RuntimeError(f" dots: {dots_count} to deep")

        struct = _struct
    ic(">>>>>>>>>",struct)
    return struct
        

def get_struct_parent(struct_get):
    parent_struct_get = struct_get("struct_parent")
    ic(parent_struct_get)
    return parent_struct_get

def get_struct_helper(id_struct,env):
    struct_get = env[id_struct]
    if struct_get is None:
        raise RuntimeError(f"Struct with name {id_struct} does not exists")
    return struct_get

def get_item_from_struct(struct_get,id_entry):
    value = struct_get("struct_env").get(id_entry)
    if value is None:
        parent_struct_get = struct_get("struct_env").get("struct_parent")
        while parent_struct_get is not None:
            value = parent_struct_get("struct_env").get(id_entry)
            _parent_struct_get = get_struct_parent(parent_struct_get)
            parent_struct_get = _parent_struct_get
    return value



@dataclass
class StructVariableFromOutside(InterpretedExpression):
    id_struct:str
    dots_count:int
    id_entry:str
    def eval(self, env: Env):
        id_struct_get = get_struct_helper(self.id_struct,env)
        id_struct_or_parent_struct_get = get_struct_x_parent_or_self_struct(id_struct_get,self.dots_count)
        if id_struct_or_parent_struct_get is None:
            raise RuntimeError(f"{self.dots_count}")
        x = get_item_from_struct(id_struct_or_parent_struct_get,self.id_entry)
        return x, env

class StructCallFunctionFromOutside(InterpretedExpression):
    def __init__(self,) -> None:
        ic("=============h17==================")
        ic("=============h17==================")
        ic("=============h17==================")
        pass

        # super().__init__()
# TODO HEREHREHREHRH
class StructCallNParentWithFunExpression(InterpretedExpression):
    def __init__(self,dot_expr, fun_args):
        self.id_struct,self.dots_count, self.entry = dot_expr
        self.args_function = fun_args

    def eval(self,env,is_struct=True):
        parent_struct = None
        value_ret =  None
        # ic(self.id_struct)
        # ic(env[self.id_struct])
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

