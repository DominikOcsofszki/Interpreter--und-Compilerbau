from icecream import ic
from top_parser import parser, lexer
# from environment import Env
# from top_imports import env_imports
from top_imports import environment
from top_load_check_file import data

print(parser.parse(input=data,lexer=lexer).eval(environment))
exit()

# env = Env(env_imports)

print(parser.parse(input=data,lexer=lexer).eval(environment))
# print(parser.parse(input=data,lexer=lexer,debug=True).eval(env))
exit()

# result = parser.parse(input=data)
# result = parser.parse(input=i,lexer=lexer)
# print("=",result.eval(env), "\t\t",env)
#
while True:
    i=input("> ")
    # result = parser.parse(input=data)
    result = parser.parse(input=i,lexer=lexer)
    # print("=",result.eval(env), "\t\t",env)
    print("=",*result.eval(environment))
    # print("=",result.eval(env), "\t\t")
    # print("=>",result.eval(env)[0], "\t\t")
    # print(env)
