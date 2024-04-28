# same as previous parser (g) but with generator for expression objects

from ply.yacc import yacc
from bools_lexer import tokens
# import g_expressions
import bools_expressions_class
# TODO: 
#     ISSUE!!! LEXER is also gettign imported. how to combine two lexer????
    # we do not only import tokens but also the rest in that modul
# tokens = tokens_arithmetic_lexer + tokens_number_lexer
print(tokens)

### the generator
# these items are expected to be implemented in module generate (see below)
used_procedures_and_classes={"BooleanExpression", "ParenExpression", \
        "NegExpression", "EqExpression", "OrExpression", "AndExpression", "NotExpression"}
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

# precedence = [['left', 'PLUS', 'MINUS'],
#               ['left', 'TIMES', 'DIVIDE']]
#

#         'not':'not', 'and':'and', 'or':'or', 'eq':'eq', 'neg':'neq',
def p_expression_boolean(p):
    'expression : true '
    p[0] = gen.BooleanExpression(p[1])

def p_expression_paren(p):
    'expression : lparen expression rparen'
    p[0] = gen.ParenExpression(p[2])

def p_error(p):
    print("Syntax error in input!")


def p_expression_not(p):
    'expression : expression not expression'
    p[0] = gen.NotExpression(p[1],p[3])

def p_expression_eq(p):
    'expression : expression eq expression'
    p[0] = gen.EqExpression(p[1],p[3])


def p_expression_or(p):
    'expression : expression or expression'
    p[0] = gen.OrExpression(p[1],p[3])

def p_expression_and(p):
    'expression : expression and expression'
    p[0] = gen.AndExpression(p[1],p[3])

def p_expression_neg(p):
    'expression : neg expression'
    p[0] = gen.NeqExpression(p[2])

### the REPL

# set_generator_module(g_expressions)
set_generator_module(bools_expressions_class)
check_generator_module()

# parser = yacc(start='expression')

parser = yacc(start='expression')
# result = parser.parse(input="true and true")
result = parser.parse(input="true and true")
print(result.eval())
exit()

https://docs.python.org/3/library/operator.html

# parser picks automatically the last lexer.
# => Import also run the whole program but only hands over the imported var.

while True:
    i=input("repl > ")
    result = parser.parse(input=i)
    print(i,"=",result.eval())
