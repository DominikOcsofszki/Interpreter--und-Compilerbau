
# '<,'>s`\(.*\)_\(.*\)Expression',`\1_\l\2(p):\r\t\t\t'expression : expression \U\2\e expression'\r\t\t\tp[0] = gen.\2Expression(p[1],p[3]) 
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

# precedence = [['left', 'PLUS', 'MINUS'],
#               ['left', 'TIMES', 'DIVIDE']]
precedence = [
    ['left', 'or'],
    ['left', 'and', 'nand'],
    ['left', 'eq', 'noteq', 'eqcomp'],
    ['left', 'lt', 'gt', 'le', 'ge'],
    # ['left', 'plus', 'minus'],
    # ['left', 'times', 'divide']
]
def p_expression_binary_operators(p):
    '''
    expression: 
                    expression xxx expression
                |   expression xxx expression
    '''
        # '!=' : 'noteq',
        # '=' : 'eqcomp',
# def p_expression_bool(p):
#     '''expression :     true 
#                     |   false'''
#     p[0] = gen.BoolExpression(p[1]) 
#
# def p_expression_and(p):
#     'expression : expression and expression'
#     p[0] = gen.AndExpression(p[1],p[3]) 
#
# def p_expression_eq(p):
#     'expression : expression eq expression'
#     p[0] = gen.EqExpression(p[1],p[3]) 
#
# def p_expression_eqcomp(p):
#     'expression : expression eqcomp expression'
#     p[0] = gen.EqCompExpression(p[1],p[3]) 
#
# def p_expression_ge(p):
#     'expression : expression ge expression'
#     p[0] = gen.GeExpression(p[1],p[3]) 
#
# def p_expression_gt(p):
#     'expression : expression gt expression'
#     p[0] = gen.GtExpression(p[1],p[3]) 
#
# def p_expression_le(p):
#     'expression : expression le expression'
#     p[0] = gen.LeExpression(p[1],p[3]) 
#     
# def p_expression_lt(p):
#     'expression : expression lt expression'
#     p[0] = gen.LtExpression(p[1],p[3]) 
#
# def p_expression_negcomp(p):
#     'expression : expression negcomp expression'
#     p[0] = gen.NotEqCompExpression(p[1],p[3]) 
#
# def p_expression_neq(p):
#     'expression : neq expression'
#     p[0] = gen.NeqExpression(p[2]) 
#
# def p_expression_not(p):
#     'expression : expression not expression'
#     p[0] = gen.NotBoolExpression(p[1]) 
#
# def p_expression_or(p):
#     'expression : expression or expression'
#     p[0] = gen.OrExpression(p[1],p[3]) 
#
# # def p_expression_paren(p):
# #     'expression : lparen expression rparen'
# #     p[0] = gen.ParenExpression(p[2])

# def p_error(p):
#     print("Syntax error in input!")

### the REPL

gen = genHelper.set_generator_module_and_check(bool_ast_class)

if __name__ == "__main__":
    tokens = tokens + tokens_bool
    lexer = lex(debug=True)
    parser = yacc(start='expression')
    while True:
        i=input("repl > ")
        result = parser.parse(input=i)
        print(i,"=",result.eval())

