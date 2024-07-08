from pack.lexer.arith_lexer import *
from pack.lexer.bool_lexer import *
from pack.lexer.write_read_lexer import *
from pack.lexer.sequences_lexer import *
from pack.lexer.control_lexer import *
from pack.lexer.local_lexer import *
from pack.lexer.lambda_lexer import *
from pack.lexer.import_lexer import *
from pack.lexer.types_lexer import *
from pack.lexer.struct_lexer import *
from ply.lex import lex
from top_configs import SHOW_TOKENS

tokens = []
literals = []

# t_ignore  = ' \t\n'
t_ignore  = ' \t'
def t_error(t):
    print("Illegal character '%s': FIX-IT" % t.value[0])
    t.lexer.skip(1)

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
    x = len(t.value)

literals=literals_arith +\
        literals_bool   +\
        literals_var    +\
        literals_sequences +\
        literals_komma +\
        literals_types

tokens = tokens 	    +\
		 tokens_arith 	+\
		 tokens_bool_new 	+\
		 tokens_var 	+\
         tokens_control+\
         tokens_local+\
         tokens_lambda+\
         tokens_import+\
         tokens_struct+\
         tokens_types
from icecream import ic
if SHOW_TOKENS:
    print(tokens)
    print(literals)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if str.upper(t.value) in tokens:
        t.type = str.upper(t.value)
    return t
def t_ignore_comments(t):
    r'[#].*'
    pass


lexer = lex()
# lexer = lex(debug=True)
