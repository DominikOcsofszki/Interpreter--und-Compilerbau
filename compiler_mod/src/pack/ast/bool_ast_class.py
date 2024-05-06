import sys
import inspect

from pack.ast.Expression import InterpretedExpression, getAllClasses

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

# print(used_procedures_and_classes)
def checkAndReturnBinaryClass(p):
    print(p[2])
    lowerp2 = p[2].lower()
    match lowerp2:
        case "and"      : p[0] = AndExpression(p[1],p[3]) 
        case "eqcomp"   : p[0] = EqCompExpression(p[1],p[3]) 
        case "="       : p[0] = EqExpression(p[1],p[3]) 
        case ">="       : p[0] = GeExpression(p[1],p[3]) 
        case ">"       : p[0] = GtExpression(p[1],p[3]) 
        case "<="       : p[0] = LeExpression(p[1],p[3]) 
        case "<"       : p[0] = LtExpression(p[1],p[3]) 
        case "not"      : p[0] = NotEqCompExpression(p[1],p[3]) 
        case "or"       : p[0] = OrExpression(p[1],p[3]) 
        case "nand"     : p[0] = NandExpression(p[1],p[3]) 
        case _ : print("STH WROMG")
    return p[0]

def checkAndReturnUnaryClass(p):
    lowerp2 = p[1].lower()
    match lowerp2:
        case "not" : p[0] = NotBoolExpression(p[2])
        case _ : print("=======errror=====")
    return p[0]

def checkAndReturnBoolValueClass(p):
    lowerp2 = p[1].lower()
    match lowerp2:
        case "true" | "false"   : p[0] = BoolValueExpression(p[1])
    return p[0]

