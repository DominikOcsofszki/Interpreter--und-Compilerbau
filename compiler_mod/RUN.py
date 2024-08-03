from icecream import ic
from src.top_parser import parser, lexer,LOAD_FILES
from src.top_imports import setup_env_for_new_file
from src.top_file_load_check import checkAndOpenFile, test_files
import CONFIGS

# NEW
import traceback
def runREPL():
    environment = setup_env_for_new_file(current_filename="")
    while True:
        i=input("> ")
        result = parser.parse(input=i,lexer=lexer)
        print("=",*result.eval(environment))

def runFromFile_code():
    data,file_name = checkAndOpenFile(file_name=LOAD_FILES)
    try:
        environment = setup_env_for_new_file(current_filename=file_name)
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
    for test_file in all_test_files:
        print("> RUN testfile: ",test_file)
        with open(test_file, 'r') as file:
            environment = setup_env_for_new_file(current_filename=test_file)
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



def get_caller_module_dict(levels):
    import sys
    f = sys._getframe(levels)
    ldict = f.f_globals.copy()
    if f.f_globals != f.f_locals:
        ldict.update(f.f_locals)
    return ldict
if __name__ == "__main__":
    run()
    # runREPL()

