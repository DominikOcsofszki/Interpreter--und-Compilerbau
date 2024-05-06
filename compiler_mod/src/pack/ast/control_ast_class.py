
from pack.ast.Expression import InterpretedExpression, getAllClasses

# loop expr do expr
# for assign;bool_expr;assign do expr
# for assign;bool_expr;assign do lock var expr << optional
# ===================================================
# if bool_expr then expr
# if bool_expr then expr else expr


class LoopExpression(InterpretedExpression):
    def __init__(self, e1):
        self.e1=e1

    def eval(self,env):
        return [expression.eval(env) for expression in self.e1]


class IfThenExpression(InterpretedExpression):
    def __init__(self, e1,e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        if self.e1.eval(env):
            return self.e2.eval(env)



class IfThenElseExpression(InterpretedExpression):
    def __init__(self, e1,e2,e3):
        self.e1=e1
        self.e2=e2
        self.e3=e3

    def eval(self,env):
        e1,env = self.e1.eval(env)
        if e1:
            e2,env = self.e2.eval(env)
            return e2
        e3 = self.e3.eval(env)
        return e3,env

class ForDoExpression(InterpretedExpression):
    def __init__(self, e1,e2,e3,e4):
        self.e1=e1
        self.e2=e2
        self.e3=e3
        self.e4=e4

    def eval(self,env):
        raise ModuleNotFoundError("asd")
        # for(e1.eval(env); e2; e3):
        #     e4.eval(env)
        # if self.e1.eval(env):
        #     return self.e2.eval(env)
        # return self.e3.eval(env)

class LoopDoExpression(InterpretedExpression):
    def __init__(self, count,body):
        self.count = count
        self.body = body

    def eval(self, env):
        #TODO: Throw Error?!?
        body = None
        count, env1 = self.count.eval(env)
        for _ in range(int(count)):
            body, env1 = self.body.eval(env1)
        return body, env1




        # for _ in range(self.count.eval(env)):
        #     self.body.eval(env)



used_procedures_and_classes = getAllClasses()

