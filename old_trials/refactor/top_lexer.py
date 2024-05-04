from pack.lexer.arith_lexer import *
from pack.lexer.bool_lexer import *
from ply.lex import lex

tokens = []
literals = []

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s': FIX-IT" % t.value[0])
    t.lexer.skip(1)

literals=literals_arith+literals_bool
tokens = tokens + tokens_arith + tokens_bool
lexer = lex(debug=True)
