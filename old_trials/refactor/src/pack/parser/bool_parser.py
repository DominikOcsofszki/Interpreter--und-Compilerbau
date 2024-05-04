
from ply.yacc import yacc
from ply.lex import lex

import pack.ast.bool_ast_class as bool_ast_class
from pack.lexer.bool_lexer import *
import pack.parser.gen_helper as gen_helper


tokens = []
#DebugMode: Change bool to True for DebugMode, False to run
gen_bool = bool_ast_class if True else None 
genHelperBool = gen_helper.GeneratorHelper(bool_ast_class.used_procedures_and_classes,gen_bool)

                    # | expression eqs expression
                    # | expression gt expression
                    # | expression lt expression
def p_expression_binary_operators(p):
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
    p[0] = gen_bool.checkAndReturnBinaryClass(p)

def p_expression_unary_operators(p):
    '''expression : not expression
    '''
    p[0] = gen_bool.checkAndReturnUnaryClass(p)

def p_expression_bool(p):
    ''' expression : BOOL'''
    p[0] = gen_bool.checkAndReturnBoolValueClass(p)

gen_bool = genHelperBool.set_generator_module_and_check(bool_ast_class)
