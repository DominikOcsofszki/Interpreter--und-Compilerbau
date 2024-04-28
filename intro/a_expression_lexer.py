# lexer to tokenize simple arithmetic expressions
# token stream is output

from ply.lex import lex

tokens = ['NUMBER', 'PLUS', 'PLUS2', 'MINUS','FLOAT']

t_PLUS    = r'\+'
t_MINUS   = r'-'

def t_FLOAT(t):
    r'\d+\.\d+'
    t.value = float(t.value)
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

def t_PLUS2(t):
    r'\+'
    print("hallo")
    return t

def t_error(t):
    print("unknown token",t)
    raise("unknown token")

lexer = lex()

lexer.input("1+2-3+4321+1")

for token in lexer:
    print(token)

lexer.input("3.14")

for token in lexer:
    print(token)
