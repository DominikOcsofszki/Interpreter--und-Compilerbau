from icecream import ic
# from pack.parser.struct_parser import P_line
from top_parser import parser, lexer
# from environment import Env
# from top_imports import env_imports
from top_imports import environment
from top_file_load_check import checkAndOpenFile

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
        print(parser.parse(input=data,lexer=lexer).eval(environment))
    except Exception as error:
        traceback.print_tb(error.__traceback__)
        ic(">>>",error,">>>")
        # traceback.format_exc()
        

# runREPL()
runFromFile_code()



