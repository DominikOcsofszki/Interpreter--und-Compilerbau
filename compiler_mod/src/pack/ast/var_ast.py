from pack.ast.Expression import InterpretedExpression, getAllClasses,ic

# def p_expression_read_id(p):
#     'expression : ID'
#     p[0] = generator_var.ReadIdExpression(p[1])
#
# def p_expression_write_id(p):
#     'expression : ID assign expression'
#     p[0] = generator_var.WriteIdExpression(p[1],p[3])

class WriteIdExpression(InterpretedExpression):
    def __init__(self, id, value):
        self.id=id
        self.value=value

    def eval(self,env):
        e2,env1 = self.value.eval(env)
        env1[self.id] = e2
        return e2, env1

class ReadIdExpression(InterpretedExpression):
    def __init__(self, id):
        self.id=id

    def eval(self,env):
        return env[self.id], env



used_procedures_and_classes = getAllClasses()

