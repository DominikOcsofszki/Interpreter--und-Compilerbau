
from ..Expression import InterpretedExpression, getAllClasses, ic

class SequenceExpression(InterpretedExpression):
    def __init__(self, seq):
        self.seq=seq

    def eval(self,env):
        r = None
        for e in self.seq:
            r, env = e.eval(env)
        return r, env



used_procedures_and_classes = getAllClasses()


