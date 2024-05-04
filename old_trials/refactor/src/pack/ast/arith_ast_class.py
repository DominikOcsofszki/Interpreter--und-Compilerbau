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

used_procedures_and_classes={
        'PlusExpression',
        'MinusExpression',
        'NumberExpression',
        'TimesExpression',
        'DivideExpression',
        'ParenExpression'
        }

