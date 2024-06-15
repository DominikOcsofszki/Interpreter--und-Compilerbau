from top_parser import parser, lexer
from environment import Env


def getFilesFromFile():
    with open('/Users/dominikocsofszki/ss2024/compiler/projekt/compiler_mod/data.tx', 'r') as file:
        # files = file.read().rstrip()
        files = file.read()
        return files

def checkFile(file:str):
    if file.startswith('#'):
        return None
    return file

def openAllFiles(files):
    for file in files.splitlines():
        if checkFile(file) :
            with open(file, 'r') as file:
                data = file.read()
                return data

files = getFilesFromFile()
data = openAllFiles(files)
print(data)
print("====================output:=======================")
env = Env()
print(parser.parse(input=data,lexer=lexer).eval(env))
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
    print("=",*result.eval(env))
    # print("=",result.eval(env), "\t\t")
    # print("=>",result.eval(env)[0], "\t\t")
    # print(env)
