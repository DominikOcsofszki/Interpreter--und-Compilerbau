from .tok_helper import tok_add_pos
def t_NEQS(t):
    r'!='
    return tok_add_pos(t)
def t_LAMBDA(t):
    r'->'
    return tok_add_pos(t)
def t_LE(t):
    r'<='
    return tok_add_pos(t)
def t_GE(t):
    r'>='
    return tok_add_pos(t)
def t_LAMBDA_START(t):
    r'\\'
    return tok_add_pos(t)
def t_EQ(t):
    r'eq'
    return tok_add_pos(t)
def t_OR(t):
    r'or'
    return tok_add_pos(t)
def t_ignore(t):
    r' \t'
    return tok_add_pos(t)
def t_AND(t):
    r'and'
    return tok_add_pos(t)
def t_NOT(t):
    r'not'
    return tok_add_pos(t)
def t_NAND(t):
    r'nand'
    return tok_add_pos(t)
def t_IMPORT(t):
    r'IMPORT'
    return tok_add_pos(t)
def t_EXTEND(t):
    r'extend'
    return tok_add_pos(t)