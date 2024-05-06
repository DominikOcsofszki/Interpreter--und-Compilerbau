from top_parser import parser, lexer

with open('/Users/dominikocsofszki/ss2024/compiler/projekt/compiler_mod/data.txt', 'r') as file:
    # data = file.read().rstrip()
    data = file.read()
# print(data)
# data ='''
# {
# y:=51;
# y:=51
# }
# '''
print(data)
env ={"x":0}
parser.parse(input=data)

result = parser.parse(input=data)
# result = parser.parse(input=i,lexer=lexer)
print("=",result.eval(env), "\t\t",env)
#
while True:
    i=input("> ")
    # result = parser.parse(input=data)
    result = parser.parse(input=i,lexer=lexer)
    # print("=",result.eval(env), "\t\t",env)
    # print("=",result.eval(env), "\t\t")
    print("=>",result.eval(env)[0], "\t\t")
    # print(env)
