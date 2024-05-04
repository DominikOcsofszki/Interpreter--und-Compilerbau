
from ply.yacc import yacc
from ply.lex import lex

from arith_parser import *
from bool_parser import *

tokens = []
precedence = []


if __name__ == "__main__":

    precedence = precedence_arith + precedence_bool
    tokens = tokens + tokens_arith + tokens_bool
    # lexer = lex(debug=True)
    lexer = lex()
    parser = yacc(start='expression')
    while True:
        # i=input("repl > ")
        i=input("> ")
        result = parser.parse(input=i)
        print(i,"=",result.eval())

