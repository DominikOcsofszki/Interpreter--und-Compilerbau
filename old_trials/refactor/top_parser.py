from pack.parser.arith_parser import *
from pack.parser.bool_parser import *
import ply.yacc as yacc
from top_lexer import tokens, lexer

# precedence =(
#         ('nonassoc', '<', '>'),
#         )
precedence = [
    # ['nonassoc', '<', '>'],
    # ['right', 'assign'],
    ['left', 'or'],
    # ['left', 'imp'],
    ['left', 'and', 'nand'],
    ['left', '=', 'neqs', 'eq'],
    # ['left', '=', 'neqs', 'eq', 'neq'],
    ['left', '<', '>', 'le', 'ge'],
    ['left', '+', '-'],
    ['left', '*', '/'],
    ['right', 'not'],
    # ['right', 'not', 'uminus', 'uplus'],
    # ['right', 'else']
]

parser = yacc.yacc(start='expression',debug=True)


