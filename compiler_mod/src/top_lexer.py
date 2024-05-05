from pack.lexer.arith_lexer import *
from pack.lexer.bool_lexer import *
from pack.lexer.var_lexer import *
from pack.lexer.sequences_lexer import *
from ply.lex import lex

tokens = []
literals = []

t_ignore  = ' \t'

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
		 tokens_sequences

lexer = lex(debug=True)
