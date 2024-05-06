
from pack.ast.Expression import InterpretedExpression, getAllClasses

class SequenceExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return [expression.eval(env) for expression in self.e1]




used_procedures_and_classes = getAllClasses()
