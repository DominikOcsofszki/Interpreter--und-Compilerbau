
from ..Expression import InterpretedExpression, ic

class SequenceExpression(InterpretedExpression):
    def __init__(self, sequences):
        ic(self, sequences)
        self.sequences=sequences

    def eval(self,env):
        last_result = None
        print(self.sequences)
        print(len(self.sequences))
        for sequence in self.sequences:
            ic(sequence)
            print("st")
            last_result, env = sequence.eval(env)
        return last_result, env





