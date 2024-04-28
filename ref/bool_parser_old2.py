
# '<,'>s`\(.*\)_\(.*\)Expression',`\1_\l\2(p):\r\t\t\t'expression : expression \U\2\e expression'\r\t\t\tp[0] = gen.\2Expression(p[1],p[3]) 
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
    '''expression :  expression AND expression
                    | expression EQ expression
                    | expression EQCOMP expression
                    | expression GE expression
                    | expression GT expression
                    | expression LE expression
                    | expression LT expression
                    | expression NOTEQCOMP expression
                    | expression OR expression
    '''
    p[0] = gen.checkAndReturnClass(p)
    # match p[2]:
    #     case "all" : p[0] = gen.checkAndReturnClass(p)
        # case "and" : p[0] = gen.AndExpression(p[1],p[3]) 
        # case "eqcomp" : p[0] = gen.EqCompExpression(p[1],p[3]) 
        # case "eq" : p[0] = gen.EqExpression(p[1],p[3]) 
        # case "ge" : p[0] = gen.GeExpression(p[1],p[3]) 
        # case "gt" : p[0] = gen.GtExpression(p[1],p[3]) 
        # case "le" : p[0] = gen.LeExpression(p[1],p[3]) 
        # case "lt" : p[0] = gen.LtExpression(p[1],p[3]) 
        # case "not" : p[0] = gen.NotEqCompExpression(p[1],p[3]) 
        # case "or" : p[0] = gen.OrExpression(p[1],p[3]) 
        #

def p_expression_unary_operators(p):
    '''expression : expression BOOL expression
                    | expression PAREN expression
                    | expression NOTBOOL expression
                    | expression NEQ expression


'''
    match p[2]:
        case "bool" : p[0] = gen.BoolExpression(p[1]) 
        case "paren" : p[0] = gen.ParenExpression(p[1]) 
        case "" : p[0] = gen.NotBoolExpression(p[1]) 
        case "" : p[0] = gen.NeqExpression(p[1]) 

gen = genHelper.set_generator_module_and_check(bool_ast_class)

if __name__ == "__main__":
    tokens = tokens + tokens_bool
    lexer = lex(debug=True)
    parser = yacc(start='expression')
    while True:
        i=input("repl > ")
        result = parser.parse(input=i)
        print(i,"=",result.eval())
# # def p_expression_div(p):
# #     'expression : expression DIVIDE expression'
# #     p[0] = gen.DivideExpression(p[1],p[3])
# #     p[0] = gen.DivideExpression(p[1],p[3])
#     p[0] = p[1] - p[3]
#
#
# 			p[0] = gen.AndExpression(p[1],p[3]) 
# 			p[0] = gen.BoolExpression(p[1],p[3]) 
# 			p[0] = gen.EqCompExpression(p[1],p[3]) 
# 			p[0] = gen.EqExpression(p[1],p[3]) 
# 			p[0] = gen.GeExpression(p[1],p[3]) 
# 			p[0] = gen.GtExpression(p[1],p[3]) 
# 			p[0] = gen.LeExpression(p[1],p[3]) 
# 			p[0] = gen.LtExpression(p[1],p[3]) 
# 			p[0] = gen.NeqExpression(p[1],p[3]) 
# 			p[0] = gen.NotBoolExpression(p[1],p[3]) 
# 			p[0] = gen.NotEqCompExpression(p[1],p[3]) 
# 			p[0] = gen.OrExpression(p[1],p[3]) 
# 			p[0] = gen.ParenExpression(p[1],p[3]) 
#         			| expression AND expression
#         			| expression BOOL expression
#         			| expression EQ expression
#         			| expression EQCOMP expression
#         			| expression GE expression
#         			| expression GT expression
#         			| expression LE expression
#         			| expression LT expression
#         			| expression NEQ expression
#         			| expression NOTBOOL expression
#         			| expression NOTEQCOMP expression
#         			| expression OR expression
#         			| expression PAREN expression
#
