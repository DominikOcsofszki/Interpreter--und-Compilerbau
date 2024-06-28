tokens_arith = ['NUMBER']

literals_arith ='+-*/()'

def t_NUMBER(t):
    r'\d+(\.\d*)?  | \.\d+'
    if '.' in t.value :
        t.value = float(t.value)
        t.type = "FLOAT"
    else:
        t.value =int(t.value)
        t.type = "NUMBER"


    return t

