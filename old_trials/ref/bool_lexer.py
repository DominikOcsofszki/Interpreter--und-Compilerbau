from ply.lex import lex

reserved_compare = {
        '<' : 'lt',
        '>' : 'gt',
        '<=' : 'le',
        '>=' : 'ge',
        '!=' : 'noteqcomp',
        '=' : 'eqcomp',
        }
reserved_bool_op ={
        'not':'not',
        'and':'and',
        'or':'or',
        'eq':'eq',
        'nand':'nand',
        }
reserved_bool_id ={
        "true":"true",
        "false":"false",
        }

tokens_bool = [
        ] + \
        list(reserved_bool_id.values()) +\
        list(reserved_compare.values()) +\
        list(reserved_bool_op.values())

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type =    reserved_bool_id.get(t.value)  or\
                reserved_bool_op.get(t.value)  
    return t

def t_RES(t):
    r'[<,<=,>,>=,!=,=]'
    t.type =    reserved_compare.get(t.value)
    return t





if __name__ == "__main__":
    t_ignore  = ' \t\n'
    tokens = tokens_bool
    print(tokens)



    def t_error(t):
        print("Illegal character '%s'" % t.value[0])
        t.lexer.skip(1)

    data = """ 
    true true true false < not  
    """

    lexer = lex()
    # Give the lexer some input
    lexer.input(data)

    # Tokenize
    while True:
        tok = lexer.token()
        if not tok:
            break      # No more input
        print(tok)

