
from typing import Match
from ply.yacc import yacc
from ply.lex import lex

import bool_ast_class
from bool_lexer import *
import gen_helper


tokens = []
#DebugMode: Change bool to True for DebugMode, False to run
gen = bool_ast_class if True else None 
# gen = None
genHelper = gen_helper.GeneratorHelper(bool_ast_class.used_procedures_and_classes,gen)

# print(tokens_bool)
# lex: tokens   = ['true', 'false', 'lt', 'gt', 'le', 'ge', 'noteqcomp', 'eqcomp', 'not', 'and', 'or', 'eq', 'nand']
precedence = [
    ['left', 'or'],
    ['left', 'and', 'nand'],
    ['left', 'eq', 'noteqcomp', 'eqcomp'],
    ['left', 'lt', 'gt', 'le', 'ge'],
    ['left', 'not'],
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
    '''
    p[0] = gen.checkAndReturnBinaryClass(p)

def p_expression_unary_operators(p):
    '''expression :   expression  expression
    '''
    p[0] = gen.checkAndReturnBoolValueClass(p)

def p_expression_bool(p):
    '''expression :   false 
                    | true

    '''
    p[0] = gen.checkAndReturnBoolValueClass(p)

gen = genHelper.set_generator_module_and_check(bool_ast_class)

if __name__ == "__main__":
    t_ignore  = ' \t\n'
    tokens = tokens + tokens_bool
    lexer = lex(debug=True)
    parser = yacc(start='expression')
    while True:
        i=input("repl > ")
        result = parser.parse(input=i)
        print(i,"=",result.eval())


# '<,'>s`\(.*\)_\(.*\)Expression',`\1_\l\2(p):\r\t\t\t'expression : expression \U\2\e expression'\r\t\t\tp[0] = gen.\2Expression(p[1],p[3]) 
