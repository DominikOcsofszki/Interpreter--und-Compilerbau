from icecream import ic
from src.top_parser import parser, lexer,LOAD_FILES
from src.top_imports import setup_env_for_new_file
from src.top_file_load_check import checkAndOpenFile, test_files
import CONFIGS

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
        environment = setup_env_for_new_file()
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
        current_filename = file
        print(">testfile: ",file)
        with open(file, 'r') as file:
            environment = setup_env_for_new_file()
            data = file.read()
        try:
            parser.parse(input=data,lexer=lexer).eval(environment)
            if CONFIGS.SHOW_ENV_AFTER_TEST_RUN:
                ic("===========================================")
                ic(">>>global/top env after run:",environment)
                ic("===========================================")
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

def get_caller_module_dict(levels):
    import sys
    f = sys._getframe(levels)
    ldict = f.f_globals.copy()
    if f.f_globals != f.f_locals:
        ldict.update(f.f_locals)
    return ldict
if __name__ == "__main__":
    # ic(get_caller_module_dict(0)['environment'])
    run()
    # ic(get_caller_module_dict(0)['environment'])
    # env_final = get_caller_module_dict(0)['environment']
    # ic(env_final['y'])
    # # for x in env_final.keys():
    # #     ic(x)
    # ic("done")

