import CONFIGS

passed_tests = []
failed_tests = []
def padding(txt):
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
    return "\033[0m"

    
def print_all_test_results():
    print("|- ======================================================")
    print("|- =====================TESTS============================")
    print("|- ======================================================")
    print("|- TODO: get info from Node, atm only latest")
    print(f"{col_g()}mPassed Tests:{col_off()}")  # Green

    for test in passed_tests:
        if "[IMP]" in test[2]:
            print(f"{col_g()}|- {test[2]!r}{padding(test[2])} {test[:-1]}{col_off()}")
        else:
            print(f"{col_g()}|-{col_off()} {test[2]!r}{padding(test[2])} {test[:-1]}")
    print(f"{col_r()}Failed Tests:{col_off()}")  # Red
    for test in failed_tests:
        if "[IMP]" in test[2]:
            print(f"{col_r()}|- {test[2]!r}{padding(test[2])} {test[:-1]}{col_off()}")
        else:
            print(f"{col_r()}|-{col_off()} {test[2]!r}{padding(test[2])} {test[:-1]}")

    print("======================================================")
    print("================END-TESTS=============================")
    print("======================================================")

def test_assert(arr_bool_and_msg, my_helper):
    msg = *arr_bool_and_msg, my_helper['tok']
    test_bool = arr_bool_and_msg[0] == arr_bool_and_msg[1]
    if not test_bool: 
        failed_tests.append(msg)
    else:
        passed_tests.append(msg)
