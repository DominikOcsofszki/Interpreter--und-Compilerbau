from ..ast import arith_ast

from ..ast import arith_ast
from ..ast.arith_ast import *

from .. import gen_helper

generator_arith = arith_ast if True else None 
genHelperArith = gen_helper.GeneratorHelper(arith_ast.used_procedures_and_classes,generator_arith)

def p_expression_binary_operators_arith(p):
    '''expression :   expression "+" expression
                    | expression "-" expression
                    | expression '*' expression
                    | expression '/' expression
    '''
    match p[2]:
        case "+"   : p[0] = PlusExpression(p[1],p[3]) 
        case "-"   : p[0] = MinusExpression(p[1],p[3]) 
        case "*"   : p[0] = TimesExpression(p[1],p[3]) 
        case "/"   : p[0] = DivideExpression(p[1],p[3]) 
        case _ : print("STH WROMG")

    # p[0] = generator_arith.checkAndReturnBinaryClass(p)

def p_expr_uminus(p):
    'expression : "-" expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_num(p):
    'expression : NUMBER'
    p[0] = generator_arith.NumberExpression(p[1])


# def p_expression_paren(p):
#     'expression : "(" expression ")"'
#     p[0] = generator_arith.ParenExpression(p[2])


generator_arith = genHelperArith.set_generator_module_and_check(arith_ast)
