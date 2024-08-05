
from ..Expression import InterpretedExpression, ic

class SequenceExpression(InterpretedExpression):
    def __init__(self, sequences):
        self.sequences=sequences

    def eval(self,env,is_struct=False):
        last_result = None
        for sequence in self.sequences:
            last_result, env = sequence.eval(env,is_struct)
        return last_result, env





