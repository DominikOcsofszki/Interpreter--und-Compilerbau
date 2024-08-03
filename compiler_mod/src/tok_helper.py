from .top_configs import PRINT_LEXER_TOK_LINE_AND_NR
my_helper = {'tok':{
    'line':0,
    'nr':0, 
    'entry':None
    }
}

print_later_arr = []
from icecream import ic
def my_print_t1(t):
    if PRINT_LEXER_TOK_LINE_AND_NR:
        print_later_arr.append(t)
        arr = print_later_arr
        # ic(arr)
        i = [f"{arr[i].type[:3]}({arr[i].value})" if i!=10 and i != 20 else f"{arr[i].type}({arr[i].value})\n>\t" for i in range(len(print_later_arr))]
        # x = [f"{x.line},{x.nr} {x.value}:{x.type} || " for x in print_later_arr]
        # x = [f"{x.type}:{x.value} || " for x in print_later_arr]
        x = [f"{x.type}:{x.value}>" for x in print_later_arr]
        x = [f"{x.type}({x.value})" for x in print_later_arr]
        # x = [f"{x.value}({x.type})" for x in print_later_arr]
        # print(*x)
        print(">>>\t",*i)
        print('')
        # print(f"{t.line},{t.nr} {t.value}:{t.type}")
def my_print_t(t):
    if PRINT_LEXER_TOK_LINE_AND_NR:
        print_later_arr.append(t)
        x = [f"{x.type}:{x.value}>" for x in print_later_arr]
        x = [f"{x.type}({x.value})" for x in print_later_arr]
        # print(*x)
        # print('')
        # print(f"{t.line},{t.nr} {t.value}({t.type})")
        print(f"{t.value}({t.type},l:{t.line},w:{t.nr})")
        # ic(print_later_arr)

#TODO switch to dynamic arr
pos_dict = [-1]*1000
def tok_add_pos(t):
    t.line = my_helper['tok']['line']
    t.nr = my_helper['tok']['nr']
    # pos_dict[t.lexpos] = [t.line,t.nr]
    pos_dict[t.lexpos] = t
    # ic(t.nr)
    my_helper['tok']['nr'] +=1
    #TODO rework
    # my_print_t(t)
    # global current_filename
    # if pos_dict[82] != -1:
    #     ic(pos_dict[82].__dict__)
    #     ic(pos_dict[82].nr)
    return t


def fun_for_t(reg,t_name):
    if reg == '\\\\':
        print(reg)
        reg ='\\'
        print(reg)
    return f'''
def {t_name}(t):
    r{reg!r}
    return tok_add_pos(t)'''

def load_dict_no_function_t_(current_file_should_be_top_lexer):
    cur_dict = current_file_should_be_top_lexer
    all_t= {t for t in cur_dict if "t_" in t}
    regex_t_not_functions = \
            {key: value for key, value in cur_dict.items() if key in all_t and not callable(value)}

    new = [fun_for_t(value,key) for key, value in regex_t_not_functions.items()]
    return new
def sort_tokens_by_length_of_doc_string(e:str):
    return len(e.splitlines()[2])

def changes_to_file(new):
    import os
    directory = os.path.dirname("src/top_tok_to_t_function.py")
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    with open("src/top_tok_to_t_function.py", "w") as file:
        file.write("from .tok_helper import tok_add_pos")
        new.sort(key=sort_tokens_by_length_of_doc_string)
        for x in new:
            for a in x:
                file.write(a)

