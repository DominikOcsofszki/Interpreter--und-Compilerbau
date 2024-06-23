
# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class StructExpression(InterpretedExpression):
    def __init__(self, entries):
        self.entries=entries

    def eval(self,env):
        lambda_env = Env(env.deep_copy())
        for entry in self.entries:
            tmp, lambda_env = entry.eval(lambda_env)
        def get(val):
            res,envv = val.eval(lambda_env)
            return res
        return get, env

class StructCallExpression(InterpretedExpression):
    def __init__(self, id, entry):
        self.entry=entry
        self.id=id

    def eval(self,env):
        struct, env = self.id.eval(env)
        return struct(self.entry), env

class StructCallFunExpression(InterpretedExpression):
    def __init__(self, struct_self, attribute,args):
        self.struct_self=struct_self
        self.attribute_func=attribute
        self.args=args

    def eval(self,env):
        struct, env = self.struct_self.eval(env)
        if len(self.args)!=0:
            args = [arg.eval(env)[0] for arg in self.args]
            return struct(self.attribute_func)(args), env

        return struct(self.attribute_func)(), env

import pack.ast.var_ast as var_ast
class StructExtendExpression(InterpretedExpression):
    def __init__(self,parent, entries):
        self.entries=entries
        self.parent=var_ast.ReadIdExpression(parent)

    def eval(self,env):
        lambda_env = Env(env.deep_copy())
        for entry in self.entries:
            tmp, lambda_env = entry.eval(lambda_env)
        lambda_env["parent"] = self.parent.eval(lambda_env)[0]
        def get(val):
            res,envv = val.eval(lambda_env)
            return res
        return get, env

# class StructCallParentExpression(InterpretedExpression):
#     def __init__(self, id, entry,n_parent):
#         ic(self, id, entry,n_parent)
#         self.entry=entry
#         self.id=id
#         self.n_parent=n_parent
#
#     def eval(self,env):
#         struct, env = self.id.eval(env)
#         entry, env = self.entry.eval(env)
#         parent = var_ast.ReadIdExpression("parent")
#         return struct(parent)(self.entry), env

class StructCallNParentExpression(InterpretedExpression):
    def __init__(self, id, entry,n_parent):
        ic(self, id, entry,n_parent)
        self.entry=entry
        self.id=id
        self.n_parent=n_parent
        self.parentString_as_readExpression = var_ast.ReadIdExpression("parent")

    def eval(self,env):
        struct, env = self.id.eval(env)
        if self.n_parent > 0:
            parent_struct = struct(self.parentString_as_readExpression)
            for i in range(self.n_parent-1):
                ic(parent_struct(self.entry))
                parent_struct = parent_struct(self.parentString_as_readExpression)
            return parent_struct(self.entry), env
        return struct(self.entry), env
        # return struct(self.parentString_as_readExpression)(self.entry), env

class StructCallNParentExpression(InterpretedExpression):
    def __init__(self, id, entry,n_parent):
        # ic(self, id, entry,n_parent)
        self.entry=entry
        self.id=id
        self.n_parent=n_parent
        self.parentString_as_readExpression = var_ast.ReadIdExpression("parent")

    def eval(self,env):
        struct, env = self.id.eval(env)
        value_ret =  struct(self.entry)
        parent_struct = struct(self.parentString_as_readExpression)
        if self.n_parent > 0:
            # parent_struct = struct(self.parentString_as_readExpression)
            for i in range(self.n_parent-1):
                parent_struct = parent_struct(self.parentString_as_readExpression)
            value_ret =  parent_struct(self.entry)

        if value_ret == None:
            ic(value_ret)
            ic(parent_struct)
            while parent_struct:
                last_struct = parent_struct
                parent_struct = parent_struct(self.parentString_as_readExpression)
            value_ret =  last_struct(self.entry)

        return value_ret, env



used_procedures_and_classes = getAllClasses()

