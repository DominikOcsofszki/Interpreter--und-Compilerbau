
from pack.ast import types_ast
from pack.ast.types_ast import *

import pack.parser.gen_helper as gen_helper


generator_local = types_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(types_ast.used_procedures_and_classes,generator_local)

def p_expression_types_float(p):
    'expression : float'
    p[0] = generator_local.FloatExpression(p[1])

def p_expression_types_string(p):
    'expression : string '
    p[0] = generator_local.StringExpression(p[1])

def p_expression_types_char(p):
    'expression : char '
    p[0] = generator_local.CharExpression(p[1])

def p_expression_types_array_assign(p):
    'expression : "[" expression_list "]"'
    p[0]=generator_local.ArrayExpression(p[2])

def p_expression_types_list(p):
    'expression : "(" expression_list ")"'
    p[0]=generator_local.ListExpression(p[2])
def p_expr_list(p):
    """
    expression_list : expression
                      | expression "," expression_list
                      | ID "," expression_list
    """
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        # p[0] = [generator_local.StringExpression(p[1]), *p[3]]
        p[0] = [p[1], *p[3]]

generator_local = genHelperVar.set_generator_module_and_check(types_ast)
