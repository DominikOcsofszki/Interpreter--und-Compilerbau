
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class SequenceExpression(InterpretedExpression):
    def __init__(self, seq):
        self.seq=seq

    def eval(self,env):
        r = None
        for e in self.seq:
            ic(e)
            r, env = e.eval(env)
        ic("=============================")
        return r, env



used_procedures_and_classes = getAllClasses()


