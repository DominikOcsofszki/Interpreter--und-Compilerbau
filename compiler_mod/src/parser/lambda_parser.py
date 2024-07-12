

from src.ast import lambda_ast
from src.ast.lambda_ast import *

from .. import gen_helper


gen = lambda_ast if True else None 
genFix = gen_helper.GeneratorHelper(lambda_ast.used_procedures_and_classes,gen)

def p_expression_expr_list(p):
    '''expression_list : expression "," expression_list
        |        expression
    '''
    p[0] = [p[1]] if len(p) ==2 else [p[1], *p[3]]

def p_expression_lambda_args_WORKING(p):
    '''expression :     LAMBDA_START LAMBDA expression
            |           LAMBDA_START expression_list  LAMBDA expression
    '''
    if len(p) == 4:
        p[0] = gen.LambdaArgsExpression([], p[3])
    if len(p) == 5:
        p[0] = gen.LambdaArgsExpression(p[2], p[4])

def p_expression_call_args(p):
    '''expression : ID "(" ")"     
        |           ID "(" expression_list ")"
    '''
    if len(p) == 4:
        p[0] = gen.CallExpression(p[1],[])
    else:
        p[0] = gen.CallExpression(p[1],[*p[3]])
gen = genFix.set_generator_module_and_check(lambda_ast)


