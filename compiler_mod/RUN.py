from top_parser import parser, lexer, env


while True:
    i=input("> ")
    result = parser.parse(input=i,lexer=lexer)
    # print(i,"=",result.eval())
    print(env)
