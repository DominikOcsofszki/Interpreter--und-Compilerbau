
from ..ast import write_read_ast
from ..ast.write_read_ast import *

from .. import gen_helper 


generator_var = write_read_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(write_read_ast.used_procedures_and_classes,generator_var)


def p_expression_read_id(p):
    'expression : ID'
    p[0] = generator_var.ReadIdExpression(p[1])

def p_expression_read_parent_id(p):
    'expression :  dots ID'
    p[0] = generator_var.ReadParentIdExpression(p[2],p[1])


def p_expression_write_id(p):
    'expression : ID ASSIGN expression'
    p[0] = generator_var.WriteIdExpression(p[1],p[3])

def p_expression_write_id_dots(p):
    'expression : dots ID ASSIGN expression'
    p[0] = generator_var.WriteIdExpression(p[2],p[4])

generator_var = genHelperVar.set_generator_module_and_check(write_read_ast)
