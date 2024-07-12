
from src.ast import types_ast
from src.ast.types_ast import *

from .. import  gen_helper


generator_local = types_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(types_ast.used_procedures_and_classes,generator_local)

def p_expression_types_float(p):
    'expression : FLOAT'
    p[0] = generator_local.FloatExpression(p[1])

def p_expression_types_string(p):
    'expression : STRING '
    p[0] = generator_local.StringExpression(p[1])

def p_expression_types_char(p):
    'expression : CHAR '
    p[0] = generator_local.CharExpression(p[1])

def p_expression_types_array(p):
    'expression : "[" expression_list "]"'
    p[0]=generator_local.ArrayExpression(p[2])

def p_expression_types_array_call(p):
    'expression : ID "[" NUMBER "]"'
    p[0]=generator_local.ArrayCallExpression(p[1],p[3])

def p_expression_types_list(p):
    'expression : "(" expression_list ")"'
    p[0]=generator_local.ListExpression(p[2])

generator_local = genHelperVar.set_generator_module_and_check(types_ast)
