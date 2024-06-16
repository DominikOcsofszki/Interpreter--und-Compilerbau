
from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses, ic

class CallDeepExpression(InterpretedExpression):
    def __init__(self, id, ids):
        self.id=id
        self.ids=ids

    def eval(self,env):


used_procedures_and_classes = getAllClasses()

