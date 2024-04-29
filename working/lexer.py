from arith_lexer import *
from bool_lexer import *
from ply.lex import lex

tokens = []
# precedence = []

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

tokens = tokens + tokens_arith + tokens_bool
lexer = lex(debug=True)
