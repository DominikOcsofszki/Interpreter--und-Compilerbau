# "BooleanExpression", "ParenExpression", "NeqExpression", "EqExpression", "OrExpression", "AndExpression", "NotExpression",
# "InterpretedExpression:
# <, >, <=, >=, !=, =

class InterpretedExpression:
    def eval(self):
        pass

class NotExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self):
        return self.e1.eval() != self.e2.eval()

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
        return self.e1.eval() == self.e2.eval()

class NegExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return not self.e1.eval()


class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return self.e1.eval()

class BooleanExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return bool(self.e1)

