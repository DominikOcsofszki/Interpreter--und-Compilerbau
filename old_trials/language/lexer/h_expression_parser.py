# same as previous parser (g) but with generator for expression objects

from ply.yacc import yacc
from old.f_expression_lexer import tokens
from arithmetic_lexer import tokens as tokens_arithmetic_lexer
from number_lexer import tokens as tokens_number_lexer
import g_expressions
# TODO: 
#     ISSUE!!! LEXER is also gettign imported. how to combine two lexer????
    # we do not only import tokens but also the rest in that modul
# tokens = tokens_arithmetic_lexer + tokens_number_lexer
print(tokens)

### the generator
# these items are expected to be implemented in module generate (see below)
used_procedures_and_classes={'PlusExpression','MinusExpression','NumberExpression',
                             'TimesExpression','DivideExpression','ParenExpression'}
gen = None

def set_generator_module(m):
    global gen
    gen = m

def generator_module_implements(used_procedures_and_classes): # check availability of module and all referenced items
    return all(hasattr(gen, x) for x in used_procedures_and_classes)

def check_generator_module():
    if not gen:
        raise Exception("No code generator provided please use 'set_generator_module()' in parser module")
    if not generator_module_implements(used_procedures_and_classes) :
        raise Exception("code generator doesn't implement all expected functions")

### the parser

precedence = [['left', 'PLUS', 'MINUS'],
              ['left', 'TIMES', 'DIVIDE']]

def p_expression_plus(p):
    'expression : expression PLUS expression'
    p[0] = gen.PlusExpression(p[1],p[3])

def p_expression_minus(p):
    'expression : expression MINUS expression'
    p[0] = gen.MinusExpression(p[1],p[3])

def p_expression_num(p):
    'expression : NUMBER'
    p[0] = gen.NumberExpression(p[1])

def p_expression_times(p):
    'expression : expression TIMES expression'
    p[0] = gen.TimesExpression(p[1],p[3])

def p_expression_div(p):
    'expression : expression DIVIDE expression'
    p[0] = gen.DivideExpression(p[1],p[3])

def p_expression_paren(p):
    'expression : LPAREN expression RPAREN'
    p[0] = gen.ParenExpression(p[2])

def p_error(p):
    print("Syntax error in input!")

### the REPL

set_generator_module(g_expressions)
check_generator_module()

parser = yacc(start='expression')

while True:
    i=input("repl > ")
    result = parser.parse(input=i)
    print(i,"=",result.eval())
