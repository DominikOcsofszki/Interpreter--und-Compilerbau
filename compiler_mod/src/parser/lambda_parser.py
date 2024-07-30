

from src.ast.lambda_ast import *
from ..Nodes import Node,Expr

def p_expression_expr_list(p):
    '''expression_list :    expression "," expression_list
                    |       expression
    '''
    if len(p) ==2:
        p[0] = [p[1]]
    else:
        p[0] = [p[1],*p[3]]

    #     p[0] = p[1], p[3]
    #     p[0] = p[1], *p[3]
    #     if len(p[3]) == 3:

def p_expression_lambda_args_WORKING(p):
    '''expression :     LAMBDA_START LAMBDA expression
            |           LAMBDA_START expression_list  LAMBDA expression
    '''
    if len(p) == 4:
        p[0] = Node(Expr.LambdaArgsExpression,[[], p[3]])
    if len(p) == 5:
        p[0] = Node(Expr.LambdaArgsExpression,[p[2], p[4]])

def p_expression_call_args(p):
    '''expression : ID "(" ")"     
        |           ID "(" expression_list ")"
    '''
    if len(p) == 4:
        p[0] = Node(Expr.CallExpression,[p[1],[]])
    else:
        p[0] = Node(Expr.CallExpression,[p[1],p[3]])



# from pack.ast import lambda_ast
# from pack.ast.lambda_ast import *
#
# import pack.parser.gen_helper as gen_helper
#
#
# gen = lambda_ast if True else None 
# genFix = gen_helper.GeneratorHelper(lambda_ast.used_procedures_and_classes,gen)
#
# def p_expression_expr_list(p):
#     '''expression_list : expression "," expression_list
#         |        expression
#     '''
#     p[0] = [p[1]] if len(p) ==2 else [p[1], *p[3]]
#
# def p_expression_lambda_args_WORKING(p):
#     '''expression :     LAMBDA_START LAMBDA expression
#             |           LAMBDA_START expression_list  LAMBDA expression
#     '''
#     if len(p) == 4:
#         p[0] = gen.LambdaArgsExpression([], p[3])
#     if len(p) == 5:
#         p[0] = gen.LambdaArgsExpression(p[2], p[4])
#
# def p_expression_call_args(p):
#     '''expression : ID "(" ")"     
#         |           ID "(" expression_list ")"
#     '''
#     if len(p) == 4:
#         p[0] = gen.CallExpression(p[1],[])
#     else:
#         p[0] = gen.CallExpression(p[1],[*p[3]])
# gen = genFix.set_generator_module_and_check(lambda_ast)



