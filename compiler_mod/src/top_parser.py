from .parser.arith_parser import *
from .parser.bool_parser import *
from .parser.write_read_parser import *
from .parser.sequences_parser import *
from .parser.control_parser import *
from .parser.local_parser import *
from .parser.lambda_parser import *
from .parser.import_parser import *
from .parser.types_parser import *
from .parser.struct_parser import *

import ply.yacc as yacc
from .top_lexer import tokens, lexer

from .top_precedence import precedence

# def p_expr_uminus(p):
#     'expression : "-" expression %prec UMINUS'
#     p[0] = -p[2]

from .top_file_load_check import print_line_nr
def p_error(p):
    if parser.state == 85:
        print('\n==================================================')
        print("STATE 85 => SEMICOLON MISSING") 
        print('\n==================================================')
    else:
        stack_state_str = ' '.join([symbol.type for symbol in parser.symstack][1:])
        print('====================Parsing-Error=================')
        print_line_nr(p.lineno)
        print('Syntax error in input line', p.lineno,": \"", p.value,"\"")
        print('Parser State {}: \n{} . {}'
              .format(parser.state,
                      stack_state_str,
                      p))
        print('\n==================================================')

    exit()

parser = yacc.yacc(start='expression',debug=True)


