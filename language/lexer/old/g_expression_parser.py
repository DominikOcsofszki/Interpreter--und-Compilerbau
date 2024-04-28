# same as previous parser (f) but with expression objects that can be evaluated

from ply.yacc import yacc
from f_expression_lexer import tokens, lexer
from g_expressions import *

precedence = [['left', 'PLUS', 'MINUS'],
              ['left', 'TIMES', 'DIVIDE']]

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = PlusExpression(p[1],p[3])

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = MinusExpression(p[1],p[3])

def p_expression_num(p):
    'expression : NUMBER'
    p[0] = NumberExpression(p[1])

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = TimesExpression(p[1],p[3])

def p_expression_div(p):
    'expression : expression DIVIDE expression'
    p[0] = DivideExpression(p[1],p[3])

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = ParenExpression(p[2])

def p_error(p):
    print("Syntax error in input!")

parser = yacc(start='expression')

while True:
    i=input("repl > ")
    result = parser.parse(input=i, lexer=lexer)
    print(i,"=",result.eval())
