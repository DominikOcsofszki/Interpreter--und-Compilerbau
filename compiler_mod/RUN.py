from top_parser import parser, lexer


env ={"x":0}
while True:
    i=input("> ")
    result = parser.parse(input=i,lexer=lexer)
    print(i,"=",result.eval(env), "\t\t",env)
    # print(env)
