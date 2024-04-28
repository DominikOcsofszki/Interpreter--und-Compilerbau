# lexer and parser for simple artih. expressions
# output is parse-tree (AST) as tuples of tuples
# notice shift reduce conflicts and parser.out file

from ply.yacc import yacc
from ply.lex import lex

tokens = ['NUMBER', 'PLUS', 'MINUS']

t_PLUS    = r'\+'
t_MINUS   = r'-'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

lexer = lex()

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = (p[1], '', p[3])

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = (p[1], 'minus', p[3])

def p_expression_num(p):
    'expression : NUMBER'
    p[0] =

parser = yacc(start='expression')
result = parser.parse(input="2+3-4")
print(result)