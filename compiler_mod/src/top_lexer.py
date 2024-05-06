from pack.lexer.arith_lexer import *
from pack.lexer.bool_lexer import *
from pack.lexer.var_lexer import *
from pack.lexer.sequences_lexer import *
from pack.lexer.control_lexer import *
from ply.lex import lex

tokens = []
literals = []

t_ignore  = ' \t\n'

def t_error(t):
    print("Illegal character '%s': FIX-IT" % t.value[0])
    t.lexer.skip(1)

literals=literals_arith +\
        literals_bool   +\
        literals_var    +\
        literals_sequences

tokens = tokens 	    +\
		 tokens_arith 	+\
		 tokens_bool 	+\
		 tokens_var 	+\
		 tokens_sequences +\
         tokens_control

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    if t.value in tokens:
        t.type = t.value
        t.value = t.value
    # print(t)
    return t

lexer = lex(debug=True)
