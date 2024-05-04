from pack.ast.Expression import InterpretedExpression
class PlusExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()+self.e2.eval()

class MinusExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()-self.e2.eval()

class TimesExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()*self.e2.eval()

class DivideExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval()/self.e2.eval()

class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return self.e1.eval()

class NumberExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return int(self.e1)

# used_procedures_and_classes={
#         'PlusExpression',
#         'MinusExpression',
#         'NumberExpression',
#         'TimesExpression',
#         'DivideExpression',
#         'ParenExpression'
#         }
#
def getAllClasses():
    import inspect, sys
    classes = [name for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) 
              if obj.__module__ is __name__]
    classes_cleaned = [ clazz for clazz in classes if clazz != "InterpretedExpression" ]
    return classes_cleaned

used_procedures_and_classes = getAllClasses()

# print(used_procedures_and_classes)
def checkAndReturnBinaryClass(p):
    match p[2]:
        case "+"   : p[0] = PlusExpression(p[1],p[3]) 
        case "-"   : p[0] = MinusExpression(p[1],p[3]) 
        case "*"   : p[0] = TimesExpression(p[1],p[3]) 
        case "/"   : p[0] = DivideExpression(p[1],p[3]) 
        case _ : print("STH WROMG")
    return p[0]

# def checkParenClass(p):
#     lowerp2 = p[1].lower()
#     match lowerp2:
#         case "not" : p[0] = NotBoolExpression(p[2])
#         case _ : print("=======errror=====")
#     return p[0]
#
# def checkAndReturnNumberValueClass(p):
#     lowerp2 = p[1].lower()
#     match lowerp2:
#         case "true" | "false"   : p[0] = BoolValueExpression(p[1])
#     return p[0]

