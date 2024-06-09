
from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses

class FloatExpression(InterpretedExpression):
    def __init__(self, value):
        self.value=value

    def eval(self,env):
         float_val = self.value
         return float(float_val), env 

class CharExpression(InterpretedExpression):
    def __init__(self, value):
        self.value=value

    def eval(self,env):
        val, env = (self.value.eval(env))
        return val, env

class StringExpression(InterpretedExpression):
    def __init__(self, value):
        self.value=value

    def eval(self,env):
        return str(self.value.eval(env))

# class ArrayExpression(InterpretedExpression):
#     def __init__(self, array_list):
#         self.array_list=array_list
#
#     def eval(self,env):
#         return str(self.value.eval(env))


used_procedures_and_classes = getAllClasses()

