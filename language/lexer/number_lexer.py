import ply.lex as lex
from ply.lex import TOKEN


tokens = [
        'NUMBER'
        ] 

TOKEN_numbers = r'\d+'
@TOKEN(TOKEN_numbers)
def t_ID(t):
    t.type = 'NUMBER'    # Check for reserved words
    return t


t_ignore  = ' \t \n'
# Build the lexer
lexer = lex.lex()

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

# data = '''1 2 4
# '''
# # Give the lexer some input
# lexer.input(data)
#
# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
