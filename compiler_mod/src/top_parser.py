from pack.parser.arith_parser import *
from pack.parser.bool_parser import *
from pack.parser.var_parser import *
from pack.parser.sequences_parser import *
from pack.parser.control_parser import *
from pack.parser.local_parser import *
from pack.parser.lambda_parser import *
from pack.parser.import_parser import *
from pack.parser.types_parser import *
from pack.parser.letrec_parser import *
from pack.parser.struct_parser import *

import ply.yacc as yacc
from top_lexer import tokens, lexer

from top_precedence import precedence

def p_expr_uminus(p):
    'expression : "-" expression %prec UMINUS'
    p[0] = -p[2]

def p_error(p):
    print("Syntax error in input:",p)




parser = yacc.yacc(start='expression',debug=True)


