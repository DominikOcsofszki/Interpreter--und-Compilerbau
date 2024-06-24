
# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic
import pack.ast.var_ast as var_ast

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

class StructCallNParentExpressionWORKING(InterpretedExpression):
    def __init__(self, id, entry,n_parent):
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
            while parent_struct:
                last_struct = parent_struct
                parent_struct = parent_struct(self.parentString_as_readExpression)
            value_ret =  last_struct(self.entry)

        return value_ret, env
class StructCallNParentExpression(InterpretedExpression):
    def __init__(self, id, entry,n_dots):
        self.id=var_ast.ReadIdExpression(id)
        self.attribute=var_ast.ReadIdExpression(entry)
        self.n_parent=n_dots - 1
        self.parentString_as_readExpression = var_ast.ReadIdExpression("parent")

    def eval(self,env):
        parent_struct = None
        value_ret =  None
        struct,env = self.id.eval(env)
        if self.n_parent > 0:
            parent_struct = struct(self.parentString_as_readExpression)
            for _ in range(self.n_parent-1):
                parent_struct = parent_struct(self.parentString_as_readExpression)
            value_ret =  parent_struct(var_ast.ReadIdExpression(self.attribute))
        else:
            return struct(self.attribute),env

        if not value_ret:
            if not parent_struct:
                    parent_struct = struct(self.parentString_as_readExpression)
            while parent_struct and not value_ret:
                value_ret = parent_struct(self.attribute)
                parent_struct = parent_struct(self.parentString_as_readExpression)

        return value_ret, env


class StructCallNParentWithFunExpression(InterpretedExpression):
    def __init__(self,arr, fun_args):
        id, entry,n_dots, = arr
        self.id=var_ast.ReadIdExpression(id)
        self.attribute=var_ast.ReadIdExpression(entry)
        self.n_parent=n_dots - 1
        self.parentString_as_readExpression = var_ast.ReadIdExpression("parent")
        self.fun_args = fun_args

    def eval(self,env):
        parent_struct = None
        value_ret =  None
        struct,env = self.id.eval(env)
        if self.n_parent > 0:
            parent_struct = struct(self.parentString_as_readExpression)
            for _ in range(self.n_parent-1):
                parent_struct = parent_struct(self.parentString_as_readExpression)
            value_ret =  parent_struct(var_ast.ReadIdExpression(self.attribute))
        else:
            return struct(self.attribute),env

        if not value_ret:
            if not parent_struct:
                    parent_struct = struct(self.parentString_as_readExpression)
            while parent_struct and not value_ret:
                value_ret = parent_struct(self.attribute)
                parent_struct = parent_struct(self.parentString_as_readExpression)

        if not self.fun_args == None:
            fun_args = [x.eval(env)[0] for x in self.fun_args]
            return value_ret(fun_args),env
        return value_ret, env

used_procedures_and_classes = getAllClasses()

