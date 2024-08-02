from icecream import ic
from ply.lex import Token
from src.top_parser import parser, lexer,LOAD_FILES
from src.top_imports import environment
from src.top_file_load_check import checkAndOpenFile, test_files

# NEW
import traceback
def runREPL():
    while True:
        i=input("> ")
        result = parser.parse(input=i,lexer=lexer)
        print("=",*result.eval(environment))

def runFromFile_code():
    if 'code/tests/' in LOAD_FILES:
        runAllTest_code()
        return
    data = checkAndOpenFile(file_name=LOAD_FILES)
    ic(data)
    try:
        print(parser.parse(input=data,lexer=lexer).eval(environment))
    except Exception as error:
        traceback.print_tb(error.__traceback__)
        ic(">>>",error,">>>")
        # traceback.format_exc()
        
def runAllTest_code():
    if 'code/tests/' in LOAD_FILES:
        print("=======================")
        print("===> RUN TEST FILES <==")
        print("=======================")
        print(LOAD_FILES)
        print("=======================")
    # data = checkAndOpenFile(file_name=LOAD_FILES)
    all_test_files = test_files(LOAD_FILES)
    for file in all_test_files:
        print(">testfile: ",file)
        with open(file, 'r') as file:
            data = file.read()
            # return data

        try:
            # print(parser.parse(input=data,lexer=lexer).eval(environment))
            parser.parse(input=data,lexer=lexer).eval(environment)
        except Exception as error:
            traceback.print_tb(error.__traceback__)
            ic(">>>",error,">>>")
            # traceback.format_exc()
# runAllTest_code()
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
