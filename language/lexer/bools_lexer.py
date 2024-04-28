# <, >, <=, >=, !=, =
# not, and, or, eq, xor[/neq, nand, nor, imp]
# false, true

import re


import ply.lex as lex
from ply.lex import TOKEN


compare = {
        '<' : 'c_smaller',
        '>' : 'c_greater',
        '<=' : 'c_smaller_equal',
        '>=' : 'c_greater_equal',
        '!=' : 'c_unequal',
        '=' : 'c_equal',
        }
bools ={
        'not':'not',
        'and':'and',
        'or':'or',
        'eq':'eq',
        'neg':'neg',
        }
boolval = {'true':'true',
        'false':'false'
        }
extra = {'(':'lparen',
           ')':'rparen'
         }
tokens = [
        'IDENTIFIER'
        ] + \
        list(compare.values()) + \
        list(bools.values()) +\
        list(extra.values()) +\
        list(boolval.values())

        # list(arithmetic.values()) + \

TOKEN_extra = r'[(,)]+'
TOKEN_compare = r'[<,>,=,<=,>=,!=]+'
# TOKEN_arithmetic = r'[+,-,/,*]+'
TOKEN_bools = r'[not,and,or,eq,xor]+'
TOKEN_bool_val = r'[true,false]+'

@TOKEN(TOKEN_extra)
def t_EXTRA(t):
    # t.type = boolval.get(t.value.lower())    # Check for reserved words
    t.type = bools.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

def t_BOOL_VAL(t):
    # t =t.lower()
    r'[true,false]+'
    # t.type = boolval.get(t.value.lower())    # Check for reserved words
    t.type = boolval.get(t.value.lower(),'IDENTIFIER')    # Check for reserved words
    return t
# @TOKEN(TOKEN_bool_val)
# def t_BOOL_VAL(t):
#     # t.type = boolval.get(t.value.lower())    # Check for reserved words
#     t.type = boolval.get(t.value.lower(),'IDENTIFIER')    # Check for reserved words
#     return t

@TOKEN(TOKEN_bools)
def t_BOOLS(t):
    # t.type = bools.get(t.value)    # Check for reserved words
    t.type = bools.get(t.value,'IDENTIFIER')    # Check for reserved words
    # t.type = bools.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

# @TOKEN(TOKEN_arithmetic)
# def t_ARITHMETIC(t):
#     # t.type = bools.get(t.value,'IDENTIFIER')    # Check for reserved words
#     t.type = bools.get(t.value)    # Check for reserved words
#     return t
@TOKEN(TOKEN_bools)
def t_COMPARE(t):
    t.type = bools.get(t.value)    # Check for reserved words
    # t.type = bools.get(t.value,'IDENTIFIER')    # Check for reserved words
    return t

t_ignore  = ' \t\n'
# Build the lexer
lexer = lex.lex(reflags=re.IGNORECASE)
#
#
# # data = '''
# # begin
# # asd()
# #     comment factorial - algol 60;
# #     integer procedure factorial(n); integer n;
# #     begin
# #         integer i,fact;
# #         fact:=1;
# #         for i:=2 step 1 until n do
# #             fact:=fact*i;
# #         factorial:=fact
# #     end;
# #     integer i;
# #     for i:=1 step 1 until 10 do outinteger(1,factorial(i));
# #     outstring(1,"\n")
# # end
# # '''
# data ='''
# falsE
# true 
#
# '''
# # Give the lexer some input
# lexer.input(data)
#
# # Tokenize
# while True:
#     tok = lexer.token()
#     if not tok:
#         break      # No more input
#     print(tok)
