
# from ply.yacc import yacc
# from ply.lex import lex

import pack.ast.bool_ast as bool_ast
from pack.lexer.bool_lexer import *
import pack.parser.gen_helper as gen_helper


tokens = []
#DebugMode: Change bool to True for DebugMode, False to run
generator_bool = bool_ast if True else None 
genHelperBool = gen_helper.GeneratorHelper(bool_ast.used_procedures_and_classes,generator_bool)

def p_expression_binary_operators_bool(p):
    '''expression :   expression and expression
                    | expression eq expression
                    | expression '=' expression
                    | expression '>' expression
                    | expression '<' expression
                    | expression ge expression
                    | expression le expression
                    | expression neqs expression
                    | expression or expression
                    | expression nand expression
    '''
    p[0] = generator_bool.checkAndReturnBinaryClass(p)

def p_expression_unary_operators(p):
    '''expression : not expression
    '''
    p[0] = generator_bool.checkAndReturnUnaryClass(p)

def p_expression_bool(p):
    ''' expression : BOOL'''
    p[0] = generator_bool.checkAndReturnBoolValueClass(p)

generator_bool = genHelperBool.set_generator_module_and_check(bool_ast)
