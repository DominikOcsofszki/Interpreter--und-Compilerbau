
from dataclasses import dataclass
from typing import List

from ..environment import Env
from ..Expression import InterpretedExpression , ic

# ============================================================
# Helper functions for Structs
# ============================================================
def _helper_get_struct_x_parent_or_self_struct(struct_get,dots_count):
    # ic("=============h32==================")
    struct = struct_get
    # ic(struct_get)
    parent_up = dots_count - 1
    for _ in range(parent_up):
        _struct = helper_get_struct_parent(struct)
        if _struct is None:
            raise RuntimeError(f" dots: {dots_count} to deep")

        struct = _struct
    return struct
        

def helper_get_struct_parent(struct_get):
    parent_struct_get = struct_get("struct_parent")
    ic(parent_struct_get)
    return parent_struct_get

def helper_get_struct_helper(id_struct,env):
    # ic("=============h31==================")
    # ic(id_struct)
    struct_get = env[id_struct]
    if struct_get is None:
        raise RuntimeError(f"Struct with name {id_struct} does not exists")
    return struct_get

def helper_get_item_from_struct(struct_get,id_entry):
    ic("=============h33==================")
    value = struct_get("struct_env").get(id_entry)
    parent_struct_get = struct_get("struct_env").get("struct_parent")
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
    def eval(self,env:Env):
        struct_env = Env(env)
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env)
        # struct_env.struct_dict = struct_env.deep_copy__only_env()
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
    def eval(self,env:Env):
        struct_env = Env(env)
        for entry in self.entries:
            tmp, struct_env = entry.eval(struct_env)
        struct_env.struct_dict = struct_env.deep_copy__only_env()
        struct_env.struct_dict["struct_parent"] = env[self.parent]
        struct_env.struct_dict["struct_env"] = struct_env.struct_dict
        def struct_get(val):
            res = struct_env.struct_dict.get(val,None)
            return res
        return struct_get, env

# def p_expression_lambda__in_struct(p):
#     '''lambda_expression_struct :   LAMBDA_START LAMBDA dots expression
#                         |           LAMBDA_START expression_list  LAMBDA dots expression
#     '''
#     if len(p) == 5:
#         p[0] = Node(Expr.LambdaStructArgsExpression,[[], p[3], p[4]])
#     if len(p) == 6:
#         p[0] = Node(Expr.LambdaStructArgsExpression,[p[2],p[4], p[5]])

    # .set_a:=\x->.a:=x;

@dataclass
class LambdaStructArgsExpression(InterpretedExpression):
    args_list:str
    dots_count:int
    expression:InterpretedExpression
    def eval(self, env: Env):
        ic(self.expression)
        ic(self.dots_count)
        ic(self.args_list[0].children,self.expression.children)
        if self.dots_count > 0:
            res = self.expression.eval(env,is_struct=True)[0]
        else:
            res = self.expression.eval(env,is_struct=False)[0]
        # ic(res)
        # exit()
        res = self.expression.eval(env,is_struct=True)[0]
        ic(self.expression)
        ic(res)
        ic("=============XXX==================")
        exit()
        # env.struct_dict[self.args_list] = res
        # id_struct_or_parent_struct_get = get_struct_x_parent_or_self_struct(self.id_struct,self.dots_count,env)
        # struct_entry = helper_get_item_from_struct(id_struct_or_parent_struct_get,self.id_entry)
        return res, env

#H_Struct
@dataclass
class AssignInStructExpression(InterpretedExpression):
    id_in_struct:str
    id_expression:InterpretedExpression
    def eval(self, env: Env):
        res = self.id_expression.eval(env)[0]
        env.struct_dict[self.id_in_struct] = res
        # id_struct_or_parent_struct_get = get_struct_x_parent_or_self_struct(self.id_struct,self.dots_count,env)
        # struct_entry = helper_get_item_from_struct(id_struct_or_parent_struct_get,self.id_entry)
        return res, env
#H_Struct
@dataclass
class StructVariableFromOutside(InterpretedExpression):
    id_struct:str
    dots_count:int
    id_entry:str
    def eval(self, env: Env):
        id_struct_or_parent_struct_get = get_struct_x_parent_or_self_struct(self.id_struct,self.dots_count,env)
        struct_entry = helper_get_item_from_struct(id_struct_or_parent_struct_get,self.id_entry)
        return struct_entry, env

@dataclass
class StructCallFunctionFromOutside(InterpretedExpression):
    id_struct:str
    dots_count:int
    id_entry:str
    args_function:List
    def eval(self, env: Env):
        id_struct_or_parent_struct_get = get_struct_x_parent_or_self_struct(self.id_struct,self.dots_count,env)
        struct_entry_func = helper_get_item_from_struct(id_struct_or_parent_struct_get,self.id_entry)

        args_function = [args_function.eval(env)[0] for args_function in self.args_function]
        # res = struct_entry_func(self.args_function)
        res = struct_entry_func(args_function)
        return res, env

@dataclass
class WriteIdStructExpression(InterpretedExpression):
    id_string: str
    value: InterpretedExpression

    def eval(self,env:Env):
        struct_env = env.struct_dict
        val = self.value.eval(env)[0]
        struct_env[self.id_string] = val
        return struct_env,env















        # ic("=============h14==================")
        # # ic("=============h12==================")
        # # ic(self.id_string)
        # # ic(self.value)
        # # ic(self.value.eval(env)[1])
        # # find_env = findEnvWithIdWrite(self.id_string,env)
        # struct_dict = env.struct_dict
        # if isinstance(self.value, str) or isinstance(self.value, int):
        #     struct_dict[self.id_string] = self.value
        #     return self.value, env
        # else:
        #     struct_dict[self.id_string] = self.value.eval(env)[0]
        #     ic(struct_dict)
        #     ic(env.struct_dict)
        #     return self.value.eval(env)[0], env
        #
