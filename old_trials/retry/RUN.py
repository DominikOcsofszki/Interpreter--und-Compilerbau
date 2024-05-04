from parser import parser

if __name__ == "__main__":
    while True:
        # i=input("repl > ")
        i=input("> ")
        result = parser.parse(input=i)
        print(i,"=",result.eval())

