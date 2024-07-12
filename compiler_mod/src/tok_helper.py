from .top_configs import PRINT_LEXER_TOK_LINE_AND_NR
my_helper = {'tok':{
    'line':0,
    'nr':0, 
    'entry':None
    }
}

print_later_arr = []

def my_print_t(t):
    if PRINT_LEXER_TOK_LINE_AND_NR:
        print_later_arr.append(t)
        # x = [f"{x.line},{x.nr} {x.value}:{x.type} || " for x in print_later_arr]
        x = [f"{x.type}:{x.value} || " for x in print_later_arr]
        print(x)
        # print(f"{t.line},{t.nr} {t.value}:{t.type}")
def tok_add_pos(t):
    t.line = my_helper['tok']['line']
    t.nr = my_helper['tok']['nr']
    my_helper['tok']['nr'] +=1
    my_print_t(t)
    return t
