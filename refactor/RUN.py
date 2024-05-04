
from top_parser import parser, lexer


while True:
    # i=input("repl > ")
    i=input("> ")
    result = parser.parse(input=i,lexer=lexer)
    # result = parser.parse(input=input("> "))
    print(i,"=",result.eval())


# if __name__ == "__main__":
#     while True:
#         # i=input("repl > ")
#         i=input("> ")
#         result = parser.parse(input=i,lexer=lexer)
#         # result = parser.parse(input=input("> "))
#         print(i,"=",result.eval())
#
