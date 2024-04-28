
from ply.yacc import yacc
from ply.lex import lex

from arith_parser import *
from bool_parser import *

tokens = []


if __name__ == "__main__":

    tokens = tokens + tokens_arith + tokens_bool
    lexer = lex(debug=True)
    parser = yacc(start='expression')
    while True:
        i=input("repl > ")
        result = parser.parse(input=i)
        print(i,"=",result.eval())

