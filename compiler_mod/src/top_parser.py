from .parser.sequences_parser import *
from .parser.control_parser import *
from .parser.local_parser import *
from .parser.lambda_parser import *
from .parser.import_parser import *
from .parser.struct_parser import *

from .parser.literals_parser import *
from .parser.binop_parser import *

import ply.yacc as yacc
from .top_lexer import tokens, lexer

from .top_precedence import precedence

def p_error(p):
    print(p.__dict__)
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

# parser = yacc.yacc(start='expression',debug=True)
parser = yacc.yacc(start='expression')

# res = parser.parse('''
#                    {
#                        x:=1;
#                        }
#
#              ''')
# print(res)
# exit()
from src.top_configs import LOAD_FILES
from .top_file_load_check import getFilesFromFile,checkFile
def print_line_nr(lineno):
    files = getFilesFromFile(LOAD_FILES)
    for file in files.splitlines():
        if checkFile(file) :
            with open(file, 'r') as file:
                linenr=1
                # data = file.read()
                for line in file:
                    if lineno == linenr:
                        print(linenr, line)
                        return 
                    linenr +=1
