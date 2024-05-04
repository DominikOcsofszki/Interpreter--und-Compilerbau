from pack.ast.Expression import InterpretedExpression

class WriteIdExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval() is  self.e2.eval()

class ReadIdExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return env[self.e1.eval()]


def getAllClasses():
    import sys
    import inspect
    classes = [name for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) 
              if obj.__module__ is __name__]
    classes_cleaned = [ clazz for clazz in classes if clazz != "InterpretedExpression" ]
    return classes_cleaned

used_procedures_and_classes = getAllClasses()
