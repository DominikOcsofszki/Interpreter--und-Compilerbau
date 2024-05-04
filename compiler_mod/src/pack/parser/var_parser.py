
from pack.ast import var_ast_class
from pack.ast.var_ast_class import *

import pack.parser.gen_helper as gen_helper


generator_var = var_ast_class if True else None 
genHelperVar = gen_helper.GeneratorHelper(var_ast_class.used_procedures_and_classes,generator_var)


def p_expression_read_id(p):
    'expression : ID'
    p[0] = generator_var.ReadIdExpression(p[1])

def p_expression_write_id(p):
    'expression : expression ASSIGN expression'
    p[0] = generator_var.WriteIdExpression(p[1],p[3])

generator_var = genHelperVar.set_generator_module_and_check(var_ast_class)
