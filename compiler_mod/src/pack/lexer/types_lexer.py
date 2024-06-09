import numpy as np
tokens_types = ['string','char','float','list','array']
literals_types = '[].'


def t_float(t):
    r'\d+\.(\d*)?'
    print("in float")
    t.value =int(t.value)
    t.type = "float"
    return t


def t_string(t):
    r'\" .*\"'
    t.value =str(t.value)
    t.type = "string"
    return t

def t_char(t):
    r"\'.\'"
    t.value =str(t.value)
    t.type = "char"
    return t


