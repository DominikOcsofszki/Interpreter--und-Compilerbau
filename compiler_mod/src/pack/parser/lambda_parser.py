

# local assignment in expr
from pack.ast import lambda_ast
from pack.ast import var_ast
from pack.ast.lambda_ast import *

import pack.parser.gen_helper as gen_helper


gen = lambda_ast if True else None 
genFix = gen_helper.GeneratorHelper(lambda_ast.used_procedures_and_classes,gen)

def p_expression_expr_list(p):
    '''expression_list : expression "," expression_list
        |        expression
    '''
    p[0] = [p[1]] if len(p) ==2 else [p[1], *p[3]]
    # if len(p) == 2:
    #     p[0] = [p[1]]
    # else:
    #     p[0] = [p[1], *p[3]]
#
#

def p_expression_lambda_args_WORKING(p):
    '''expression :     lambda_start lambda expression
            |           lambda_start expression_list  lambda expression
    '''
    if len(p) == 4:
        p[0] = gen.LambdaArgsExpression([], p[3])
    if len(p) == 5:
        p[0] = gen.LambdaArgsExpression(p[2], p[4])

# def p_expression_call_no_vars(p):
#     'expression :  ID "(" ")"'
#     p[0] = gen.CallExpression(p[1],[])
#
# def p_expression_call_args(p):
#     'expression :  ID "(" expression_list ")"'
#     p[0] = gen.CallExpression(p[1],[*p[3]])

def p_expression_call_args(p):
    '''expression : ID "(" ")"     
        |           ID "(" expression_list ")"
    '''
    if len(p) == 4:
        p[0] = gen.CallExpression(p[1],[])
    else:
        p[0] = gen.CallExpression(p[1],[*p[3]])
gen = genFix.set_generator_module_and_check(lambda_ast)





# def p_expression_lambda_args_WORKING(p):
#     '''expression :     lambda expression
#             |           expression_list  lambda expression
#             |           ID lambda expression
#             |           "(" expression_list ")" lambda expression
#     '''
#             # |           ID lambda expression
#     if len(p) == 3:
#         p[0] = gen.LambdaArgsExpression([], p[2])
#     if len(p) == 4:
#         #TODO: is this really needed!!!?????!??!??!
#         p[0] = gen.LambdaArgsExpression([var_ast.ReadIdExpression(p[1])], p[3])
#     if len(p) == 6:
#         p[0] = gen.LambdaArgsExpression(p[2], p[5])
#
#     # p[0] = gen.LambdaArgsExpression(p[2], p[5])




