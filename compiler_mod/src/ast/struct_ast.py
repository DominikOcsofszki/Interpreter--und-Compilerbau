
from dataclasses import dataclass
from typing import List

from ..environment import Env
from ..Expression import InterpretedExpression , ic

# ============================================================
# Helper functions for Structs
# ============================================================
def _helper_get_struct_x_parent_or_self_struct(struct_get,dots_count):
    struct = struct_get
    parent_up = dots_count - 1
    for _ in range(parent_up):
        _struct = helper_get_struct_parent(struct)
        if _struct is None:
            raise RuntimeError(f" dots: {dots_count} to deep")

        struct = _struct
        ic(">>>>>>>>>",struct)
    ic(">>>>>>>>>",struct)
    return struct
        

def helper_get_struct_parent(struct_get):
    parent_struct_get = struct_get("struct_parent")
    ic(parent_struct_get)
    return parent_struct_get

def helper_get_struct_helper(id_struct,env):
    struct_get = env[id_struct]
    if struct_get is None:
        raise RuntimeError(f"Struct with name {id_struct} does not exists")
    return struct_get

def helper_get_item_from_struct(struct_get,id_entry):
    value = struct_get("struct_env").get(id_entry)
    if value is None:
        parent_struct_get = struct_get("struct_env").get("struct_parent")
        while parent_struct_get is not None:
            value = parent_struct_get("struct_env").get(id_entry)
            _parent_struct_get = helper_get_struct_parent(parent_struct_get)
            parent_struct_get = _parent_struct_get
    return value

def get_struct_x_parent_or_self_struct(id_struct,dots_count,env):
    id_struct_get = helper_get_struct_helper(id_struct,env)
    id_struct_or_parent_struct_get = _helper_get_struct_x_parent_or_self_struct(id_struct_get,dots_count)
    if id_struct_or_parent_struct_get is None:
        raise RuntimeError(f"{dots_count}")
    return id_struct_or_parent_struct_get
# ============================================================
# Helper functions for Structs
# ============================================================

@dataclass
class StructExpression(InterpretedExpression):
    entries: List
    def eval(self,env:Env,is_struct=True):
        struct_env = Env(env)
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env,is_struct=True)
        struct_env.struct_dict = struct_env.deep_copy__only_env()
        struct_env.struct_dict["struct_parent"] = None 
        struct_env.struct_dict["struct_env"] = struct_env.struct_dict
        def struct_get(val):
            res = struct_env.struct_dict.get(val,None)
            return res
        return struct_get, env

@dataclass
class StructExtendExpression(InterpretedExpression):
    parent: InterpretedExpression
    entries: List
    def eval(self,env:Env,is_struct=True):
        struct_env = Env(env)
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env,is_struct=True)
        struct_env.struct_dict = struct_env.deep_copy__only_env()
        struct_env.struct_dict["struct_parent"] = env[self.parent]
        struct_env.struct_dict["struct_env"] = struct_env.struct_dict
        def struct_get(val):
            res = struct_env.struct_dict.get(val,None)
            return res
        return struct_get, env


#H_Struct
@dataclass
class StructVariableFromOutside(InterpretedExpression):
    id_struct:str
    dots_count:int
    id_entry:str
    def eval(self, env: Env, is_struct=True):
        id_struct_or_parent_struct_get = get_struct_x_parent_or_self_struct(self.id_struct,self.dots_count,env)
        struct_entry = helper_get_item_from_struct(id_struct_or_parent_struct_get,self.id_entry)
        return struct_entry, env

@dataclass
class StructCallFunctionFromOutside(InterpretedExpression):
    id_struct:str
    dots_count:int
    id_entry:str
    args_function:List
    def eval(self, env: Env, is_struct=True):
        id_struct_or_parent_struct_get = get_struct_x_parent_or_self_struct(self.id_struct,self.dots_count,env)
        struct_entry_func = helper_get_item_from_struct(id_struct_or_parent_struct_get,self.id_entry)
        ic(self.args_function)
        # ic(self.args_function)
        res = struct_entry_func(self.args_function)
        return res, env

