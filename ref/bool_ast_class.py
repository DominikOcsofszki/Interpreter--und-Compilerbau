import sys
import inspect

class InterpretedExpression:
    def eval(self):
        pass
class LtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()<self.e2.eval()

class GtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()>self.e2.eval()

class LeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()<=self.e2.eval()

class GeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()>=self.e2.eval()

class NotEqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()!=self.e2.eval()

class EqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()==self.e2.eval()
# ==================================
class AndExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval() and self.e2.eval()
class OrExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval() or self.e2.eval()
class EqExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval() is  self.e2.eval()



class NotBoolExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return not self.e1.eval()
class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return self.e1.eval()

class BoolValueExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return self.e1=="true"
class NeqExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return not self.e1.eval()

def getAllClasses():
    classes = [name for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) 
              if obj.__module__ is __name__]
    classes_cleaned = [ clazz for clazz in classes if clazz != "InterpretedExpression" ]
    return classes_cleaned

used_procedures_and_classes = getAllClasses()

print(used_procedures_and_classes)
def checkAndReturnBinaryClass(p):
    lowerp2 = p[2].lower()
    match lowerp2:
        case "and"      : p[0] = AndExpression(p[1],p[3]) 
        case "eqcomp"   : p[0] = EqCompExpression(p[1],p[3]) 
        case "eq"       : p[0] = EqExpression(p[1],p[3]) 
        case "ge"       : p[0] = GeExpression(p[1],p[3]) 
        case "gt"       : p[0] = GtExpression(p[1],p[3]) 
        case "le"       : p[0] = LeExpression(p[1],p[3]) 
        case "lt"       : p[0] = LtExpression(p[1],p[3]) 
        case "not"      : p[0] = NotEqCompExpression(p[1],p[3]) 
        case "or"       : p[0] = OrExpression(p[1],p[3]) 
    return p[0]

    # match p[2]:
    #     case "bool" : p[0] = gen.BoolValueExpression(p[1]) 
    #     case "paren" : p[0] = gen.ParenExpression(p[1]) 
    #     case "" : p[0] = gen.NotBoolExpression(p[1]) 
    #     case "" : p[0] = gen.NeqExpression(p[1]) 
def checkAndReturnUnaryClass(p):
    lowerp2 = p[2].lower()
    match lowerp2:
        case "true" : p[0] = BoolValueExpression(p[1])
        case "false" : p[0] = BoolValueExpression(p[1])

def checkAndReturnBoolValueClass(p):
    lowerp2 = p[1].lower()
    match lowerp2:
        case "true" : p[0] = BoolValueExpression(p[1])
        case "false" : p[0] = BoolValueExpression(p[1])
    return p[0]

# used_procedures_and_classes={
#         'AndExpression',
#         'BoolExpression',
#         'EqCompExpression',
#         'EqExpression',
#         'GeExpression',
#         'GtExpression',
#         'LeExpression',
#         'LtExpression',
#         'NeqExpression',
#         'NotBoolExpression',
#         'NotEqCompExpression',
#         'OrExpression',
#         'ParenExpression',
#         }
# # print(used_procedures_and_classes)
