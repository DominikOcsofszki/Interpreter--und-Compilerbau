
from ..Expression import InterpretedExpression, ic

class SequenceExpression(InterpretedExpression):
    def __init__(self, sequences):
        self.sequences=sequences

    def eval(self,env):
        last_result = None
        for sequence in self.sequences:
            last_result, env = sequence.eval(env)
        return last_result, env





