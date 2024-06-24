from pack.parser.arith_parser import *
from pack.parser.bool_parser import *
from pack.parser.var_parser import *
from pack.parser.sequences_parser import *
from pack.parser.control_parser import *
import ply.yacc as yacc
from top_lexer import tokens, lexer

# precedence123 ='''
# nonassoc assign collon
# left gt lt ge le eq neqsleft plus minues
# left times didivide 
# right uminusleft seperator
# left else
# left then
# '''

# precedence = [
#     ['nonassoc', ';', 'assign'],
#     # ['right', 'assign'],
#     ['left', 'or'],
#     # ['left', 'imp'],
#     ['left', 'and', 'nand'],
#     ['left', '=', 'neqs', 'eq'],
#     # ['left', '=', 'neqs', 'eq', 'neq'],
#     ['left', '<', '>', 'le', 'ge'],
#     ['left', '+', '-'],
#     ['left', '*', '/'],
#     ['right', 'not'],
#     # ['right', 'not', 'uminus', 'uplus'],
#     ['left', 'else'],
#     ['left', 'then']
# ]
# reserved_compare = {
#         '<=' : 'le',
#         '>=' : 'ge',
#         '!=' : 'neqs',
#         }
# reserved_bool_op ={
#         'not':'not',
#         'and':'and',
#         'or':'or',
#         'eq':'eq',
#         'nand':'nand',
#         }
# reserved_bool_values ={
#         "true":"true",
#         "false":"false",
#         }
#

# precedence =[
# ["left", "then"],
# ["left", "else"],
# ["left", "do"],
# ["right", "assign"],
# ["left", "or"],
# # ["left", "or", "nor"],
# ["left", "and", "nand"],
# # ["left",  "neq"],
# # ["left", "xor", "neq", "eq", "impl"],
# # ["left", "equals", "not_equals"],
# ["left", "eq", "neqs"],
# # ["left", "less_then", "greater_then", "less_equals", "greater_equals"],
# ["left", "<", ">", "le", "ge"],
# ["left", "+", "-"],
# ["left", "*", "/"],
# ["right", "UMINUS"],
# ["left", ";"],
#
# ]

precedence = [
    ['nonassoc', 'then'],
    ['nonassoc', 'else', 'do'],
    ['right', 'assign'],
    ['left', 'or'],
    # ['left', 'imp'],
    ['left', 'and', 'nand'],
    ['left', '=', 'neqs', 'eq', 'not'],
    ['left', '<', '>', 'le', 'ge'],
    ['left', '+', '-'],
    ['left', '*', '/'],
    ['right', 'not', 'UMINUS'],
]


# precedence =[
#
# ["left", ";"],
# ["right", "UMINUS"],
# ["left", "*", "/"],
# ["left", "+", "-"],
# ["left", "<", ">", "le", "ge"],
# ["left", "eq", "neqs"],
# ["left", "and", "nand"],
# ["left", "or"],
# ["right", "assign"],
# ["left", "do"],
# ["left", "else"],
# ["left", "then"],
#
#
#
# # ["left", "or", "nor"],
# # ["left",  "neq"],
# # ["left", "xor", "neq", "eq", "impl"],
# # ["left", "equals", "not_equals"],
# # ["left", "less_then", "greater_then", "less_equals", "greater_equals"],
#
# ]
def p_expr_uminus(p):
    'expression : "-" expression %prec UMINUS'
    p[0] = -p[2]

def p_error(p):
    print("Syntax error in input!")



# vars={}
parser = yacc.yacc(start='expression',debug=True)


