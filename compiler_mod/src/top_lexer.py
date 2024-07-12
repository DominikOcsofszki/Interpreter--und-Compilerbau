# from .lexer.arith_lexer import *
# from .lexer.bool_lexer import *
# from .lexer.write_read_lexer import *
from .lexer.sequences_lexer import *
from .lexer.control_lexer import *
from .lexer.local_lexer import *
from .lexer.lambda_lexer import *
from .lexer.import_lexer import *
# from .lexer.types_lexer import *
from .lexer.struct_lexer import *
from ply.lex import lex
from .top_configs import SHOW_TOKENS

from .lexer.literals_lexer import *

tokens = []
literals = []

# t_ignore  = ' \t\n'
t_ignore  = ' \t'
def t_error(t):
    print("Illegal character '%s': FIX-IT" % t.value[0])
    t.lexer.skip(1)

    
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



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n'
    t.lexer.lineno += len(t.value)
    lexer.my_helper['tok']['nr'] = 0
    lexer.my_helper['tok']['line'] = t.lexer.lineno

# def my_print_t(t):
#     print(f"{t.line},{t.nr} {t.value}:{t.type}")
# def tok_add_pos(t):
#     t.line = lexer.my_helper['tok']['line']
#     t.nr = lexer.my_helper['tok']['nr']
#     lexer.my_helper['tok']['nr'] +=1
#     my_print_t(t)
#     return t
from . import tok_helper
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if str.upper(t.value) in tokens:
        t.type = str.upper(t.value)
    return tok_helper.tok_add_pos(t)
    # return t
def t_ignore_comments(t):
    r'[#].*'
    pass


# lexer = lex()
lexer = lex(debug=True)

lexer.my_helper = tok_helper.my_helper
