from arith_lexer import *
from bool_lexer import *

tokens = []
precedence = []


tokens = tokens + tokens_arith + tokens_bool
lexer = lex(debug=True)

