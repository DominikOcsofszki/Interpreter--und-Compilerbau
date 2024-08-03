import CONFIGS
from icecream import ic

passed_tests = []
failed_tests = []
def padding(txt):
    padding = 30 - len(txt)
    return "_" * padding

#TODO correct this! missing other text length
            # left_side = f"{col_g()}|- {test[2]!r}{padding(test[2])} {test[:-2]}"
            # right_side = f"{padding_f_name(left_side)}{test[3]}{col_off()}"
            # print(left_side,right_side)
            #
            #
def padding_f_name(txt):
    padding = 20 - len(txt)
    return "_" * padding
def col_g():
    if not CONFIGS.COLORIZE:
        return ""
    else:
        return "\033[92m"
def col_r():
    if not CONFIGS.COLORIZE:
        return ""
    else:
        return "\033[91m"

def col_off():
    if not CONFIGS.COLORIZE:
        return ""
    return "\033[0m"

    
def print_all_test_results():
    # print("|- ======================================================")
    print(f"{col_g()}| =====================TESTS============================{col_off()}")
    # print("|- ======================================================")
    # print("|- TODO: get info from Node, atm only latest")
    print(f"{col_g()}|{col_off()}")
    print(f"{col_g()}|Passed Tests:{col_off()}")  # Green

    #TODO: ADD Check for all params added
    for test in passed_tests:
        # if "[IMP]" in test[2]:
        if "[IMP]" in test[2]:
            print(f"{col_g()}|- {test[2]!r}{padding(test[2])} {test[:-2]}{padding_f_name(test[:-3])}{test[3]}{col_off()}")
            print(f"{col_g()}|- {test[2]!r}{padding(test[2])} {test[:-2]}{padding_f_name(test[:-3])}{test[3]}{col_off()}")
        else:
                 print(f"{col_g()}|-{col_off()} {test[2]!r}{padding(test[2])}{test[:-2]}{padding_f_name(test[:-3])}{test[3]}")
    print(f"{col_r()}|{col_off()}{col_r()}Failed Tests:{col_off()}")  # Red
    for test in failed_tests:
        if "[IMP]" in test[2]:
            print(f"{col_r()}|- {test[2]!r}{padding(test[2])} {test[:-2]}{padding_f_name(test[:-3])}{test[3]}{col_off()}")
        else:
            print(f"{col_r()}|-{col_off()} {test[2]!r}{padding(test[2])} {test[:-2]}{padding_f_name(test[:-3])}{test[3]}")
    print(f"{col_g()}|{col_off()}")
    # print("======================================================")
    print(f"{col_g()}================END-TESTS============================={col_off()}")
    # print("======================================================")

def test_assert(arr_bool_and_msg, env):
    # ic("=============h12==================")
    # print(">>>",env.parent['current_filename'])
    file_name = env.parent['current_filename']
    msg = *arr_bool_and_msg, file_name
    # msg = *arr_bool_and_msg, env['tok']
    #TODO bettere comparator!!!
    test_bool = arr_bool_and_msg[0] == arr_bool_and_msg[1]
    if not test_bool: 
        failed_tests.append(msg)
    else:
        passed_tests.append(msg)

def test_false(arr_bool_and_msg, env):
    file_name = env.parent['current_filename']
    msg = *arr_bool_and_msg, file_name
    #TODO bettere comparator!!!
    test_bool = not arr_bool_and_msg[0] == arr_bool_and_msg[1]
    if not test_bool: 
        failed_tests.append(msg)
    else:
        passed_tests.append(msg)

