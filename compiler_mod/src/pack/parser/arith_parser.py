from ..ast import arith_ast

import pack.ast.arith_ast as arith_ast
from pack.ast.arith_ast import *

import pack.parser.gen_helper as gen_helper


generator_arith = arith_ast if True else None 
genHelperArith = gen_helper.GeneratorHelper(arith_ast.used_procedures_and_classes,generator_arith)

def p_expression_binary_operators_arith(p):
    '''expression :   expression "+" expression
                    | expression "-" expression
                    | expression '*' expression
                    | expression '/' expression
    '''
    p[0] = generator_arith.checkAndReturnBinaryClass(p)


def p_expression_num(p):
    'expression : NUMBER'
    p[0] = generator_arith.NumberExpression(p[1])

def p_expression_paren(p):
    'expression : "(" expression ")"'
    p[0] = generator_arith.ParenExpression(p[2])


generator_arith = genHelperArith.set_generator_module_and_check(arith_ast)
