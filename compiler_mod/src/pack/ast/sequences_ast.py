
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class SequenceExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        # ic.enable()
        r = None
        # ic(*self.e1)
        for e in self.e1:
            r, env = e.eval(env)
        return r, env
        return [expression.eval(env) for expression in self.e1]




used_procedures_and_classes = getAllClasses()


# from ast import Expression
# from pack.ast.Expression import InterpretedExpression, getAllClasses, ic
# from pack.ast.control_ast import IfThenElseExpression
# class SequenceExpression(InterpretedExpression):
#     def __init__(self, e1):
#         self.e1=e1
#
#     def eval(self,env):
#         ic.enable()
#         r = None
#         # if isinstance(self.e1, InterpretedExpression):
#         #     ic(*self.e1)
#         #     r, env = self.e1.eval(env)
#         # else:
#         ic(*self.e1)
#         for e in self.e1:
#             ic(e)
#             r, env = e.eval(env)
#         # ic.disable()
#         return r, env
#         # return [expression.eval(env) for expression in self.e1]
#
#
#
#
# used_procedures_and_classes = getAllClasses()
#
