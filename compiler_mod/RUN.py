from icecream import ic
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
    data = checkAndOpenFile(file_name=LOAD_FILES)
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
    all_test_files = test_files(LOAD_FILES)
    for file in all_test_files:
        # print(">testfile: ",file)
        with open(file, 'r') as file:
            data = file.read()
        try:
            # print(parser.parse(input=data,lexer=lexer).eval(environment))
            parser.parse(input=data,lexer=lexer).eval(environment)
        except Exception as error:
            traceback.print_tb(error.__traceback__)
            ic(">>>",error,">>>")
            # traceback.format_exc()
def run():
    if 'code/tests/' in LOAD_FILES:
        runAllTest_code()
    else:
        runFromFile_code()


# def find_column(input, token):
#     line_start = input.rfind('\n', 0, token.lexpos) + 1
#     print(token)
#     return (token.lexpos - line_start) + 1

if __name__ == "__main__":
    run()

