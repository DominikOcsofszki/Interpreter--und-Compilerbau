from pack.parser.arith_parser import *
from pack.parser.bool_parser import *
from pack.parser.var_parser import *
from pack.parser.sequences_parser import *
from pack.parser.control_parser import *
from pack.parser.local_parser import *
from pack.parser.lambda_parser import *
from pack.parser.import_parser import *
from pack.parser.types_parser import *
import ply.yacc as yacc
from top_lexer import tokens, lexer


precedence = [
    ['right', 'assign'],
    ['right', 'lambda'],
    ['nonassoc', 'then'],
    ['nonassoc', 'else', 'do'],
    # ['right', 'assign'],
    ['left', 'or'],
    # ['left', 'imp'],
    ['left', 'and', 'nand'],
    ['left', '=', 'neqs', 'eq', 'not'],
    ['left', '<', '>', 'le', 'ge'],
    ['left', '+', '-'],
    ['left', '*', '/'],
    ['right', 'not', 'UMINUS'],
    ['left', ','],
    # ['right', '[',']'],
    ['right', '(',')'],
]


def p_expr_uminus(p):
    'expression : "-" expression %prec UMINUS'
    p[0] = -p[2]

def p_error(p):
    print("Syntax error in input:",p)



# vars={}
parser = yacc.yacc(start='expression',debug=True)


