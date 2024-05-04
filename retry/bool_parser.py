
from typing import Match
from ply.yacc import yacc
from ply.lex import lex

import bool_ast_class
from bool_lexer import *
import gen_helper
# from arith_parser import *


tokens = []
#DebugMode: Change bool to True for DebugMode, False to run
gen_bool = bool_ast_class if True else None 
# gen = None
genHelperBool = gen_helper.GeneratorHelper(bool_ast_class.used_procedures_and_classes,gen_bool)

# print(tokens_bool)
# lex: tokens   = ['true', 'false', 'lt', 'gt', 'le', 'ge', 'noteqcomp', 'eqcomp', 'not', 'and', 'or', 'eq', 'nand']
# lex: tokens   = [ 'not',  'nand']
precedence_bool = [
    ['left', 'or'],
    ['left', 'and', 'nand'],
    ['left', 'eq', 'noteqcomp', 'eqcomp'],
    ['left', 'lt', 'gt', 'le', 'ge'],
    # ['left', 'not'],
    ['right', 'not'],
     # ['right', 'NOT', 'UMINUS', 'UPLUS']
]
def p_expression_binary_operators(p):
    '''expression :   expression and expression
                    | expression eq expression
                    | expression eqcomp expression
                    | expression ge expression
                    | expression gt expression
                    | expression le expression
                    | expression lt expression
                    | expression noteqcomp expression
                    | expression or expression
                    | expression nand expression
    '''
    p[0] = gen_bool.checkAndReturnBinaryClass(p)

def p_expression_unary_operators(p):
    '''expression :  not expression
    '''
    p[0] = gen_bool.checkAndReturnUnaryClass(p)

def p_expression_bool(p):
    '''expression :   false 
                    | true

    '''
    p[0] = gen_bool.checkAndReturnBoolValueClass(p)


gen_bool = genHelperBool.set_generator_module_and_check(bool_ast_class)

if __name__ == "__main__":
    from arith_parser import *
    # def p_expression_num(p):
    #     'expression : NUMBER'
    #     p[0] = gen_arith.NumberExpression(p[1])
    precedence = precedence_bool 
    t_ignore  = ' \t\n'
    tokens = tokens + tokens_bool + tokens_arith
    lexer = lex(debug=True)
    parser = yacc(start='expression',debug=True)
    while True:
        i=input("repl > ")
        result = parser.parse(input=i)
        print(i,"=",result.eval())


# '<,'>s`\(.*\)_\(.*\)Expression',`\1_\l\2(p):\r\t\t\t'expression : expression \U\2\e expression'\r\t\t\tp[0] = gen.\2Expression(p[1],p[3]) 
