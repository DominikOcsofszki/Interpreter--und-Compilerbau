# tokens_arith = ['NUMBER','FLOAT']
tokens_arith = ['NUMBER']

literals_arith ='+-*/()'

def t_NUMBER(t):
    # r'\d+'
    r'\d+(\.\d*)?'
    if '.' in t.value :
        t.value = float(t.value)
        t.type = "FLOAT"
    else:
        t.value =int(t.value)
        t.type = "NUMBER"


    return t

# tokens_arith = ['NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN']
# t_ignore  = ' \t'
#
# def t_error(t):
#     print("Illegal character '%s'" % t.value[0])
#     t.lexer.skip(1)


# t_PLUS    = r'\+'
# t_MINUS   = r'-'
# t_TIMES   = r'\*'
# t_DIVIDE  = r'/'
# t_LPAREN  = r'\('
# t_RPAREN  = r'\)'
