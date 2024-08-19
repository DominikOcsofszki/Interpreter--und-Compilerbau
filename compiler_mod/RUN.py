from icecream import ic
from ply.lex import LexToken
from src.top_parser import parser, lexer,LOAD_FILES
from src.top_imports import setup_env_for_new_file
from src.top_file_load_check import checkAndOpenFile, test_files
import CONFIGS

# global ENV_DICTS_ARR
# ENV_DICTS_ARR=[{}]
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

def print_lexer():
    data,file_name = checkAndOpenFile(file_name=LOAD_FILES)
    lexer.input(data)
    tok_arr = []
    tok_arr_all = []

    while True:
        tok: LexToken = lexer.token()
        if not tok:
            break  # No more input
        tok_arr_all.append(tok)
        # print(tok)
        # if tok.value == '}':
        #     tok_arr.append("\n")
        # # ic(tok.__dict__)
        #
        # tok_arr.append(str(tok.type))
        #
        # if tok.value == '{':
        #     tok_arr.append("\n")
        # # if tok.value == ',':
        # #     tok_arr.append(" ")
        # if tok.value == ';':
        #     tok_arr.append("\n")

        # print(tok.value)
    # print(tok_arr)
    comb = "".join(tok_arr)
    # print(comb)
    # filtered_token = [x.type for x in tok_arr_all]
    # filtered_token = [x.type +" " if x.type != ';' else ';\n' for x in tok_arr_all]

    filtered_token = [
    ';\n' if x.type == ';' else
    '\n}' if x.type == '}' else
    '{\n' if x.type == '{' else
    str(x.value) + ' '
    for x in tok_arr_all
]
    # filtered_token = [x.type if x.type != 'NEWLINE' else '\n' for x in tok_arr_all]
    comb_all = "".join(filtered_token)
    print(comb_all)
    # with open('output/output_tokenized_file.txt', 'w') as file:
    #     file.write(comb_all)


if __name__ == "__main__":
    # ic(lexer.my_helper)
    run()
    # print_lexer()
    # runREPL()
