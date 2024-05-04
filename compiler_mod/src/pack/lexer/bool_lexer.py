reserved_compare = {
        '<=' : 'le',
        '>=' : 'ge',
        '!=' : 'neqs',
        }
reserved_bool_op ={
        'not':'not',
        'and':'and',
        'or':'or',
        'eq':'eq',
        'nand':'nand',
        }
reserved_bool_values ={
        "true":"true",
        "false":"false",
        }

literals_bool ='><='

tokens_bool = ['BOOL'] + \
        list(reserved_compare.values()) +\
        list(reserved_bool_op.values())

def t_BOOL(t):
    r'true | false'
    t.type  ="BOOL"
    return t

def t_ID(t):
    r'not | and | or | eq | nand'
    t.type =    reserved_bool_op.get(t.value)
    return t

t_le=r'<='
t_ge=r'>='
t_neqs=r'!='
