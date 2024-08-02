
from .. import tok_helper


tokens_arith = ['NUMBER']
literals_arith ='+-*/()'

def t_NUMBER(t):
    # r'\d+(\.\d*)?  | \.\d+'
    r'\-?\d+(\.\d*)?  | \.\d+'
    if '.' in t.value :
        t.value = float(t.value)
        t.type = "FLOAT"
    else:
        t.value =int(t.value)
        t.type = "NUMBER"


    return tok_helper.tok_add_pos(t)
    return t

literals_bool ='><='

tokens_bool_new = ['BOOL','LE', 'GE', 'NEQS','NOT', 'AND', 'OR', 'EQ', 'NAND']
# t_LE=r'<='
# t_GE=r'>='
# t_NEQS=r'!='
# t_NOT=	r'not'
# t_AND=	r'and'
# t_OR=	r'or'
# t_EQ=	r'eq'
# t_NAND=	r'nand'
def t_BOOL(t):
    r'true | false'
    t.type  ="BOOL"
    return tok_helper.tok_add_pos(t)
    return t


tokens_types = ['STRING','CHAR','FLOAT']
literals_types = '[].\''

def t_string(t):
    r'"([^\n"]|\")*"'
    # r'\".*\"'
    t.value =t.value[1:-1]
    t.type = "STRING"
    return tok_helper.tok_add_pos(t)
    # return t

def t_char(t):
    r"'([^\n']|\')'"
    # r'''
    # \'.\'   | 
    # \'\\t\' |
    # \'\\n\'
    # '''
    t.value =t.value[1:-1] 
    t.type = "CHAR"
    return tok_helper.tok_add_pos(t)
    # return t

#def t_ID in top_parser
tokens_var = ['ID','ASSIGN']
# t_ASSIGN=r":="
def t_ASSIGN(t):
    r":="
    return tok_helper.tok_add_pos(t)

literals_var =""
