from pack.ast.Expression import InterpretedExpression, getAllClasses
class PlusExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 + e2, env2

class MinusExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 - e2, env2

class TimesExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 * e2, env2

class DivideExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

# TODO!!!!
    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        e2, env2 = self.e2.eval(env1)
        return e1 / e2, env2

class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        e1, env1 = self.e1.eval(env)
        return e1, env1
        # return self.e1.eval(env), env

class FloatExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return float(self.e1), env

class NumberExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return int(self.e1), env

used_procedures_and_classes = getAllClasses()

def checkAndReturnBinaryClass(p):
    match p[2]:
        case "+"   : p[0] = PlusExpression(p[1],p[3]) 
        case "-"   : p[0] = MinusExpression(p[1],p[3]) 
        case "*"   : p[0] = TimesExpression(p[1],p[3]) 
        case "/"   : p[0] = DivideExpression(p[1],p[3]) 
        case _ : print("STH WROMG")
    return p[0]

