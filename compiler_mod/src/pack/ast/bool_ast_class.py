import sys
import inspect

from pack.ast.Expression import InterpretedExpression
class LtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env) < self.e2.eval(env)

class GtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env)>self.e2.eval(env)

class LeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env)<=self.e2.eval(env)

class GeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env)>=self.e2.eval(env)

class NotEqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env)!=self.e2.eval(env)

class EqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env)==self.e2.eval(env)
# ==================================
class AndExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env) and self.e2.eval(env)
class OrExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env) or self.e2.eval(env)
class EqExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return self.e1.eval(env) is  self.e2.eval(env)



class NotBoolExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return not self.e1.eval(env)

class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return self.e1.eval(env)

class BoolValueExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return self.e1=="true"
class NeqExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return not self.e1.eval(env)

class NandExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        return not self.e1.eval(env) and self.e2.eval(env)

def getAllClasses():
    classes = [name for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) 
              if obj.__module__ is __name__]
    classes_cleaned = [ clazz for clazz in classes if clazz != "InterpretedExpression" ]
    return classes_cleaned

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

