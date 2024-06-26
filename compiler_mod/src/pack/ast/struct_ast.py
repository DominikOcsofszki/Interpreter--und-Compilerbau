

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
        new_parent_struct = self.parent.eval(env)[0]
        lambda_env["parent_in_struct"] = new_parent_struct
        for entry in self.entries:
            tmp, lambda_env = entry.eval(lambda_env)
        lambda_env["parent"] = self.parent.eval(lambda_env)[0]
        def get(val):
            res,envv = val.eval(lambda_env)
            return res
        return get, env


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
            value_ret =struct(self.attribute) 
            if not self.fun_args == None:
                fun_args = [x.eval(env)[0] for x in self.fun_args]
                return value_ret(fun_args),env

            return value_ret,env

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

