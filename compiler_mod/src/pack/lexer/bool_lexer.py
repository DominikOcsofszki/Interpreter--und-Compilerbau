literals_bool ='><='

tokens_bool_new = ['BOOL','LE', 'GE', 'NEQS','NOT', 'AND', 'OR', 'EQ', 'NAND']
t_LE=r'<='
t_GE=r'>='
t_NEQS=r'!='
t_NOT=	r'not'
t_AND=	r'and'
t_OR=	r'or'
t_EQ=	r'eq'
t_NAND=	r'nand'
def t_BOOL(t):
    r'true | false'
    t.type  ="BOOL"
    return t

