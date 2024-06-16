
# letrec fac := x -> fac(x) + 1

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses,ic

class LetrecExpression(InterpretedExpression):
    def __init__(self,x, value, body):
        ic(self,x, value, body)
        self.x=x
        self.value=value
        self.body=body
        # tmp=Env()
        # tmp[self.x] = body
        # self.tmp_env = tmp
        # ic(self.tmp_env)

    def eval(self,env):
        env = Env(env)
        env[self.x]=self.body
        local_value, old_val = self.value.eval(env)
        old_val = env[self.x]
        ic(old_val)
        exit()
        env[self.x] = local_value
        res, env = self.body.eval(env)
        if old_val:
            env[self.x] = old_val
        return res,env
# letrec fac := {x} -> fac(x)
    # 'expression : letrec ID assign expression lambda expression'
# class LetrecExpression(InterpretedExpression):
#     def __init__(self, assign_name, ids, body):
#         ic(self, assign_name, ids, body)
#         self.assign_name=assign_name
#         self.value=ids
#         self.body=body
# # TODO !!!!!
#     def eval(self,env):



    # def eval(self,env):
    #     local_value, tmp = self.value.eval(env)
    #     old_val = env[self.assign_name]
    #     env[self.assign_name] = local_value
    #     res, env = self.body.eval(env)
    #     if old_val:
    #         env[self.assign_name] = old_val
    #     return res,env


used_procedures_and_classes = getAllClasses()

