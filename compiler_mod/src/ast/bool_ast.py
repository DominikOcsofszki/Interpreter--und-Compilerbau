from ..Expression import InterpretedExpression, getAllClasses

class BoolValueExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return self.e1=="true", env
class LtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 < e2, env2

class GtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 > e2, env2

class LeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 <= e2, env2

class GeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 >= e2, env2

class NotEqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 != e2, env2

class EqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 == e2, env2
# ==================================
class AndExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return (e1 and e2), env2

class OrExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return (e1 or e2), env2

class EqExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return (e1 is e2), env2



class NotBoolExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        return not e1, env1

class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        e1,env1 =self.e1.eval(env)
        return e1,env1

class NeqExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        e1,env1 = self.e1.eval(env)
        return not e1, env1

class NandExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return (not (e1 and e2)), env2

used_procedures_and_classes = getAllClasses()

