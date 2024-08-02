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

def tok_add_pos(t):
    t.line = my_helper['tok']['line']
    t.nr = my_helper['tok']['nr']
    # ic(t.nr)
    my_helper['tok']['nr'] +=1
    my_print_t(t)
    return t
