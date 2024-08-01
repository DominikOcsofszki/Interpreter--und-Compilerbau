from icecream import ic
from ply.lex import Token
# from src.parser.struct_parser import P_line
from src.top_parser import parser, lexer
# from environment import Env
# from top_imports import env_imports
from src.top_imports import environment
from src.top_file_load_check import checkAndOpenFile
import src.interpreter as interpreter
# NEW
import traceback
def runREPL():
    while True:
        i=input("> ")
        result = parser.parse(input=i,lexer=lexer)
        print("=",*result.eval(environment))

def runFromFile_code():
    data = checkAndOpenFile()
    try:
        parsed_expr = parser.parse(input=data,lexer=lexer)
        # ic(parsed_expr)
        print_last_and_env = interpreter.eval(parsed_expr,environment)
        ic(print_last_and_env)
        # print(parsed_expr.eval(environment))
        # print(parser.parse(input=data,lexer=lexer).eval(environment))
    except Exception as error:
        traceback.print_tb(error.__traceback__)
        ic(">>>",error,">>>")
        # traceback.format_exc()
        

# runREPL()
runFromFile_code()

def find_column(input, token):
    line_start = input.rfind('\n', 0, token.lexpos) + 1
    print(Token)
    return (token.lexpos - line_start) + 1

# def sth():
#     data = '''
# 3 + 4 * 10
# x
#       '''
#         # Give the lexer some input
#     lexer.input(data)
#
#     # Tokenize
#     while True:
#         tok = lexer.token()
#         if not tok: 
#             break      # No more input
#         print(find_column(data, tok))
#         print(tok)
#
# sth()
#
