
from ..environment import Env
from ..Expression import InterpretedExpression, getAllClasses, ic

class LocalNewExpression(InterpretedExpression):
    def __init__(self, assign_ID, assign_right_expr, expression_in):
        self.assign_ID=assign_ID
        self.assign_right_expr=assign_right_expr
        self.expression_in=expression_in

    def eval(self,env):
        env[self.assign_ID] = self.assign_right_expr
        res, env = self.expression_in.eval(env)
        res, env = res.eval(env)
        return res, env

class LocalExpression(InterpretedExpression):
    def __init__(self, var, value, body):
        self.var=var
        self.value=value
        self.body=body

    def eval(self,env):
        env1 = Env(env)
        val, env2 = self.value.eval(env1)
        env2[self.var] = val
        res, local_env = self.body.eval(env2)
        return res, env

used_procedures_and_classes = getAllClasses()

