









tokens_arith = ['NUMBER']

literals_arith ='+-*/()'

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
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
