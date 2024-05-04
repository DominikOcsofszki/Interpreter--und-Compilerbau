from arith_parser import *
from bool_parser import *
import ply.yacc as yacc
from lexer import tokens

precedence = precedence_arith + precedence_bool

parser = yacc.yacc(start='expression',debug=True)


