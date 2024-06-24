tokens_var = ['ID','ASSIGN']
t_ASSIGN=r":="

literals_var =""

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = 'ID'
    return t

