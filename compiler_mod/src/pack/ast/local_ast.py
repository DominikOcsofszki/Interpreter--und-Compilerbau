# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

# class LocalExpression(InterpretedExpression):
#     def __init__(self, assign_to_id, value, body):
#         self.assign_to_id=assign_to_id
#         self.value=value
#         self.body=body
#
#     def eval(self,env):
#         local_value, old_val = self.value.eval(env)
#         old_val = env[self.assign_to_id]
#         env[self.assign_to_id] = local_value
#         res, env = self.body.eval(env)
#         if old_val:
#             env[self.assign_to_id] = old_val
#         return res,env
#

# def p_expression_local(p):
#     'expression : local ID assign expression in expression'
#     p[0] = generator_local.LocalNewExpression(p[2],p[4],p[6])

# def p_expression_local(p):
#     'expression : local ID assign expression in expression'
#     p[0] = generator_local.LocalNewExpression(p[2],p[4],p[6])
#
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

