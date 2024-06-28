tokens_types = ['STRING','CHAR','FLOAT']
literals_types = '[].\''

def t_string(t):
    r'\".*\"'
    t.value =t.value[1:-1]
    t.type = "STRING"
    return t

def t_char(t):
    r'''
    \'.\'   | 
    \'\\t\' |
    \'\\n\'
    '''
    t.value =t.value[1:-1] 
    t.type = "CHAR"
    return t


