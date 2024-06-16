
from pack.ast.Expression import InterpretedExpression, getAllClasses,ic

# loop expr do expr
# for assign;bool_expr;assign do expr
# for assign;bool_expr;assign do lock var expr << optional
# ===================================================
# if bool_expr then expr
# if bool_expr then expr else expr


# class LoopExpression(InterpretedExpression):
#     def __init__(self, e1):
#         self.e1=e1
#
#     def eval(self,env):
#         e1
#         return [expression.eval(env) for expression in self.e1]
#

class IfThenExpression(InterpretedExpression):
    def __init__(self, e1,e2):
        self.e1=e1
        self.e2=e2

    def eval(self,env):
        e1,env = self.e1.eval(env)
        if e1:
            return self.e2.eval(env)
        return None, env



class IfThenElseExpression(InterpretedExpression):
    def __init__(self, comparator,expr1,expr2):
        self.comparator=comparator
        self.expr1=expr1
        self.expr2=expr2

    def eval(self,env):
        comp_eval,env = self.comparator.eval(env)
        if comp_eval:
            e2,env = self.expr1.eval(env)
            return e2,env
        e3 = self.expr2.eval(env)
        return e3,env

class WhileExpression(InterpretedExpression):
    def __init__(self,comparator,body):
        self.comparator=comparator
        self.body=body

    def eval(self,env):
        _,env  = self.comparator.eval(env)
        result = None
        while True :
            condition, env = self.comparator.eval(env)
            if not condition:
                break
            result, env = self.body.eval(env)
        return result,env

class ForDoExpression(InterpretedExpression):
    def __init__(self, init_assign,condition,re_assign,body):
        self.init_assign=init_assign
        self.condition=condition
        self.re_assign=re_assign
        self.body=body

    def eval(self,env):
        _,env  = self.init_assign.eval(env)
        result = None
        while True :
            condition, env = self.condition.eval(env)
            if not condition:
                break
            result, env = self.body.eval(env)
            _, env = self.re_assign.eval(env)
        return result,env



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

