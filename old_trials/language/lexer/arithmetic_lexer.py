# <, >, <=, >=, !=, =
# not, and, or, eq, xor[/neq, nand, nor, imp]
# false, true



import ply.lex as lex
from ply.lex import TOKEN


compare = {
        '<' : 'c_smaller',
        '>' : 'c_greater',
        '<=' : 'c_smaller_equal',
        '>=' : 'c_greater_equal',
        '!=' : 'c_unequal',
        '=' : 'c_equal',
        }
arithmetic = {
        r'+' : 'PLUS',
        '-' : 'MINUS',
        '/' : 'DIVIDE',
        '*' : 'TIMES',
        '('  : 'LPAREN',
        ')'  : 'RPAREN'
        }
bools ={
        'not':'not',
        'and':'and',
        'or':'or',
        'eq':'eq',
        'xor':'xor',
        }
tokens = [
        # 'IDENTIFIER'
        ] + \
        list(arithmetic.values()) 

        # list(compare.values())

#
# TOKEN_compare = r'[<,>,=,<=,>=,!=]+'
# TOKEN_arithmetische = r'[+,-,/,*]+'
# TOKEN_bools = r'[not,and,or,eq,xor]+'
# # @TOKEN(TOKEN_bools)
# @TOKEN(TOKEN_arithmetische)
# # @TOKEN(TOKEN_compare)
# def t_ID(t):
#     ignore_case = t.value.lower()
#     t.type = arithmetic.get(ignore_case,'IDENTIFIER')    # Check for reserved words
#     # t.type = arithmetic.get(t.value,'IDENTIFIER')    # Check for reserved words
#     return t
#
#
# # Build the lexer
# lexer = lex.lex()
