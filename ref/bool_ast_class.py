class InterpretedExpression:
    pass
    # def eval(self):
    #     pass
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
class NotBoolExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return not self.e1.eval()
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
class NeqExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return not self.e1.eval()

class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return self.e1.eval()

class BoolExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self):
        return self.e1=="true"

used_procedures_and_classes={
        'AndExpression',
        'BoolExpression',
        'EqCompExpression',
        'EqExpression',
        'GeExpression',
        'GtExpression',
        'LeExpression',
        'LtExpression',
        'NeqExpression',
        'NotBoolExpression',
        'NotEqCompExpression',
        'OrExpression',
        'ParenExpression',
        }

        # 'InterpretedExpression'

        # 'AndExpression'
        # 'BoolExpression'
        # 'EqCompExpression'
        # 'EqExpression'
        # 'GeExpression'
        # 'GtExpression'
        # 'LeExpression'
        # 'LtExpression'
        # 'NeqExpression'
        # 'NotBoolExpression'
        # 'NotEqCompExpression'
        # 'OrExpression'
        # 'ParenExpression'
