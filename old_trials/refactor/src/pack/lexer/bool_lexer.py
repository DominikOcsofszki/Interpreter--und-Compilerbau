# from ply.lex import lex



reserved_compare = {
        # '<' : 'lt',
        # '>' : 'gt',
        # '=' : 'eqs',
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

tokens_bool = [
        'BOOL',
        # 'ID'
        ] + \
        list(reserved_compare.values()) +\
        list(reserved_bool_op.values())


# t_lt=r'<'
# t_gt=r'>'
# t_eqs=r'='
t_le=r'<='
t_ge=r'>='
t_neqs=r'!='



def t_BOOL(t):
    r'true | false'
    t.type  ="BOOL"
    return t

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type =    reserved_bool_op.get(t.value, "ID")
    return t

# def t_RES1(t):
#     r'[<,>,=]'
#     print(t)
#     t.type =    reserved_compare.get(t.value)
#     return t

# def t_RES2(t):
#     r'[<=,>=,!=]'
#     print(t)
#     t.type =    reserved_compare.get(t.value)
#     return t
