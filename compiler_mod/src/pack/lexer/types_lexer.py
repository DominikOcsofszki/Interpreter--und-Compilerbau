import numpy as np
tokens_types = ['string','char','float','list','array']
literals_types = '[].\''

# def t_float(t):
#     # r'\d+(\.\d*)?'
#     r'\d+[.]+(\d*)?'
#     # r'\d+\.'
#     print("in float")
#     t.value =float(t.value)
#     t.type = "float"
#     return t


def t_string(t):
    r'\".*\"'
    t.value =t.value[1:-1]
    t.type = "string"
    return t

def t_char(t):
    r'''
    \'.\'   | 
    \'\\t\' |
    \'\\n\'
    '''
    t.value =t.value[1:-1] 
    t.type = "char"
    return t


