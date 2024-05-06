from pack.ast.Expression import InterpretedExpression, getAllClasses

class WriteIdExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e2,env1 = self.e2.eval(env)
        env1[self.e1] = e2
        return e2, env1

class ReadIdExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return env[self.e1], env



used_procedures_and_classes = getAllClasses()

