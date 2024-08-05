from ..Expression import InterpretedExpression, getAllClasses, ic

class PlusExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return (e1 + e2), env2

class MinusExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return (e1 - e2), env2

class TimesExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env)
        # e2, env2 = self.e2.eval(env,is_struct1,is_struct)
        return (e1 * e2), env2

class DivideExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

# TODO!!!!
    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return (e1 / e2), env2

class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        return e1, env1
        # return self.e1.eval(env,is_struct), env

class FloatExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env,is_struct=False):
        return float(self.e1), env

class NumberExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env,is_struct=False):
        return int(self.e1), env

class BoolValueExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env,is_struct=False):
        return self.e1=="true", env
class LtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return e1 < e2, env2

class GtExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return e1 > e2, env2

class LeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return e1 <= e2, env2

class GeExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return e1 >= e2, env2

class NotEqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return e1 != e2, env2

class EqCompExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return e1 == e2, env2
# ==================================
class AndExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return (e1 and e2), env2

class OrExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return (e1 or e2), env2

class EqExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return (e1 is e2), env2



class NotBoolExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        return not e1, env1

class ParenExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env,is_struct=False):
        e1,env1 =self.e1.eval(env,is_struct)
        return e1,env1

class NeqExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env,is_struct=False):
        e1,env1 = self.e1.eval(env,is_struct)
        return not e1, env1

class NandExpression(InterpretedExpression):
    def __init__(self, e1, e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1, env1 = self.e1.eval(env,is_struct)
        e2, env2 = self.e2.eval(env1,is_struct)
        return (not (e1 and e2)), env2


