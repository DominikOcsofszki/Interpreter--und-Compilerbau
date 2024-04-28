# <, >, <=, >=, !=, =
# not, and, or, eq, xor[/neq, nand, nor, imp]
# false, true



import ply.lex as lex
import ply.yacc as yacc
from ply.lex import TOKEN


compare = {
        '<' : 'c_smaller',
        '>' : 'c_greater',
        '<=' : 'c_smaller_equal',
        '>=' : 'c_greater_equal',
        '!=' : 'c_unequal',
        '=' : 'c_equal',
        }
arithmetische = {
        '+' : 'plus',
        '-' : 'minus',
        '/' : 'divide',
        '*' : 'mult',
        }
bools ={
        'not':'not',
        'and':'and',
        'or':'or',
        'eq':'eq',
        'xor':'xor',
        }
tokens = [
        'IDENTIFIER'
        ] + \
        list(arithmetische.values()) + \
        list(compare.values())


TOKEN_id = r'[<,>,=,<=,>=,!=]+'
TOKEN_arithmetische = r'[+,-,/,*]+'
TOKEN_bools = r'[not,and,or,eq,xor]+'
@TOKEN(TOKEN_bools)
@TOKEN(TOKEN_arithmetische)
@TOKEN(TOKEN_bools)
def t_ID(t):
    t.type = arithmetische.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t


# Build the lexer
lexer = lex.lex()



from ply.lex import lex


def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore  = ' \t'

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex()

