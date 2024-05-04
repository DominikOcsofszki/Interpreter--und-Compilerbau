# same as previous parser (d) but with precedence rules
# correct result
# no shift reduce conflicts

from ply.yacc import yacc
from ply.lex import lex

tokens = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN']

t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex()

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
input = "(2-3)*4/43-21"
result = parser.parse(input=input)
print(input,"=",result)

input = "1+2*3+4"
result = parser.parse(input=input, lexer=lexer)
print(input,"=",result)