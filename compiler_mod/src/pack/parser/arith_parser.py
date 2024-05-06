# from ..lexer import arith_lexer
from ..ast import arith_ast_class
# import sys;sys.path.append("..")
#
# from ply.yacc import yacc
# from ply.lex import lex

import pack.ast.arith_ast_class as arith_ast_class
from pack.ast.arith_ast_class import *

# import pack.lexer.arith_lexer as arith_lexer
import pack.parser.gen_helper as gen_helper


#DebugMode: Change bool to True for DebugMode, False to run
generator_arith = arith_ast_class if True else None 
# gen_arith = None
genHelperArith = gen_helper.GeneratorHelper(arith_ast_class.used_procedures_and_classes,generator_arith)

# precedence_arith = [['left', '+', '-'],
#               ['left', '*', '/']]

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

# def p_error(p):
#     print("Syntax error in input!")

### the REPL

generator_arith = genHelperArith.set_generator_module_and_check(arith_ast_class)

# if __name__ == "__main__":
#     tokens = []
#     precedence = precedence_arith
#     tokens = tokens + tokens_arith
#     lexer = lex(debug=True)
#     parser = yacc(start='expression')
#     while True:
#         i=input("repl > ")
#         result = parser.parse(input=i)
#         print(i,"=",result.eval())
#
# precedence_arith = [['left', 'PLUS', 'MINUS'],
#               ['left', 'TIMES', 'DIVIDE']]
#
# def p_expression_plus(p):
#     'expression : expression PLUS expression'
#     p[0] = gen_arith.PlusExpression(p[1],p[3])
#
# def p_expression_minus(p):
#     'expression : expression MINUS expression'
#     p[0] = gen_arith.MinusExpression(p[1],p[3])
#
# def p_expression_num(p):
#     'expression : NUMBER'
#     p[0] = gen_arith.NumberExpression(p[1])
#
# def p_expression_times(p):
#     'expression : expression TIMES expression'
#     p[0] = gen_arith.TimesExpression(p[1],p[3])
#
# def p_expression_div(p):
#     'expression : expression DIVIDE expression'
#     p[0] = gen_arith.DivideExpression(p[1],p[3])
#
# def p_expression_paren(p):
#     'expression : LPAREN expression RPAREN'
#     p[0] = gen_arith.ParenExpression(p[2])
#
