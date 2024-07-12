
my_helper = {'tok':{
    'line':0,
    'nr':0, 
    'entry':None
    }
}


def my_print_t(t):
    if(False):
        print(f"{t.line},{t.nr} {t.value}:{t.type}")
def tok_add_pos(t):
    t.line = my_helper['tok']['line']
    t.nr = my_helper['tok']['nr']
    my_helper['tok']['nr'] +=1
    my_print_t(t)
    return t
