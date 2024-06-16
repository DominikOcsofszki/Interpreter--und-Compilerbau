

# local assignment in expr
from pack.ast import lambda_ast
from pack.ast.lambda_ast import *

import pack.parser.gen_helper as gen_helper


gen = lambda_ast if True else None 
genFix = gen_helper.GeneratorHelper(lambda_ast.used_procedures_and_classes,gen)

def p_expression_lambda(p):
    '''expression : ID lambda expression
    |   lambda expression
    '''
    if len(p) == 3:
        p[0] = gen.LambdaNoVarsExpression(p[2])
    else:
        p[0] = gen.LambdaExpression(p[1],p[3])


def p_expression_expr_ids2(p):
    '''id_list : expression "," id_list
        |           expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1], *p[3]]


def p_expression_lambda_args(p):
    'expression : "(" id_list ")" lambda expression'
    p[0] = gen.LambdaArgsExpression(p[2],p[5])

def p_expression_call_no_vars(p):
    'expression :  ID "(" ")"'
    p[0] = gen.CallExpression(p[1],[])

def p_expression_call_args(p):
    'expression :  ID "(" id_list ")"'
    p[0] = gen.CallExpression(p[1],[*p[3]])

gen = genFix.set_generator_module_and_check(lambda_ast)

