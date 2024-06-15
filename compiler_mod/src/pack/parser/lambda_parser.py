

# local assignment in expr
from pack.ast import lambda_ast
from pack.ast.lambda_ast import *

import pack.parser.gen_helper as gen_helper


generator_local = lambda_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(lambda_ast.used_procedures_and_classes,generator_local)

def p_expression_lambda(p):
    'expression : ID lambda expression'
    p[0] = generator_local.LambdaExpression(p[1],p[3])


def p_expression_expr_ids2(p):
    '''id_list : ID "," id_list
        |           expression
    '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1], *p[3]]
    ic(">>p_expression_expr_ids2: ",p[0])


def p_expression_lambda_args(p):
    'expression : "(" id_list ")" lambda expression'
    p[0] = generator_local.LambdaArgsExpression(p[2],p[5])


def p_expression_call_args(p):
    'expression :  ID "(" id_list ")"'
    p[0] = generator_local.CallExpression(p[1],p[3])
    ic(">: ",p[0])

generator_local = genHelperVar.set_generator_module_and_check(lambda_ast)

