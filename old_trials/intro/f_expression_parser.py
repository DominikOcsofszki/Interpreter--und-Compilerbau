# same parser as before (g) but lexer and parser split into two modules
# notice import of token list from lexer and passing of lexer to parse method

from ply.yacc import yacc
from f_expression_lexer import tokens, lexer

precedence = [['left', 'PLUS', 'MINUS'],
              ['left', 'TIMES', 'DIVIDE']]

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = p[1]+ p[3]

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = p[1]- p[3]

def p_expression_num(p):
    'expression : NUMBER'
    p[0] = int(p[1])

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = p[1]* p[3]

def p_expression_div(p):
    'expression : expression DIVIDE expression'
    p[0] = p[1] / p[3]

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = p[2]

def p_error(p):
    print("Syntax error in input!")

parser = yacc(start='expression')
input = "1+2*3+4"
result = parser.parse(input=input, lexer=lexer)
print(input,"=",result)