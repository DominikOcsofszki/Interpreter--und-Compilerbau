
from ..Expression import InterpretedExpression, getAllClasses,ic


class IfThenExpression(InterpretedExpression):
    def __init__(self, e1,e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env,is_struct=False):
        e1,env = self.e1.eval(env,is_struct)
        if e1:
            return self.e2.eval(env,is_struct)
        return None, env



class IfThenElseExpression(InterpretedExpression):
    def __init__(self, comparator,expr1,expr2):
        self.comparator=comparator
        self.expr1=expr1
        self.expr2=expr2

    def eval(self,env,is_struct=False):
        comp_eval,env = self.comparator.eval(env,is_struct)
        if comp_eval:
            e2,env = self.expr1.eval(env,is_struct)
            return e2,env
        #TODO: THIis!!!!
        # e3 = self.expr2.eval(env)
        e3,env = self.expr2.eval(env,is_struct)
        return e3,env

class WhileExpression(InterpretedExpression):
    def __init__(self,comparator,body):
        self.comparator=comparator
        self.body=body

    def eval(self,env,is_struct=False):
        _,env  = self.comparator.eval(env,is_struct)
        result = None
        while True :
            condition, env = self.comparator.eval(env,is_struct)
            if not condition:
                break
            result, env = self.body.eval(env,is_struct)
        return result,env

class ForDoExpression(InterpretedExpression):
    def __init__(self, init_assign,condition,re_assign,body):
        self.init_assign=init_assign
        self.condition=condition
        self.re_assign=re_assign
        self.body=body

    def eval(self,env,is_struct=False):
        _,env  = self.init_assign.eval(env,is_struct)
        result = None
        while True :
            condition, env = self.condition.eval(env,is_struct)
            if not condition:
                break
            result, env = self.body.eval(env,is_struct)
            _, env = self.re_assign.eval(env,is_struct)
        return result,env



class LoopDoExpression(InterpretedExpression):
    def __init__(self, count,body):
        self.count = count
        self.body = body

    def eval(self, env,is_struct=False):
        #TODO: Throw Error?!?
        body = None
        count, env1 = self.count.eval(env,is_struct)
        for _ in range(int(count)):
            body, env1 = self.body.eval(env1,is_struct)
        return body, env1


used_procedures_and_classes = getAllClasses()

