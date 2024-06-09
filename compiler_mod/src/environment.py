from os import error


class Env:

    def __init__(self,parent=None) -> None:
        self.parent = parent
        self.env_dict={}

    def __contains__(self,key):
        if key in self.env_dict:
            return True
        elif self.parent:
            return key in self.parent
        return False

# //TODO!!!
    def __repr__(self) -> str:
        if self.parent:
            return str(self.env_dict) + str(self.parent )
        return str(self.env_dict)


    def __getitem__(self,key):
        # if type(key) is int: #or key.isdigit():
        #     return int(key)
        if key in self.env_dict:
            return self.env_dict[key]
        elif self.parent:
            return self.parent[key]
        return None

    def __setitem__(self,key,value):
        self.env_dict[key]=value

    #
    # def define_local(self, name, value):
    #     self.dict_env[name] = value
    #
    # def push(self):
    #     return Environment(self)
    # 
    # def pop(self):
    #     return self.parent

# a = "asd"
# b = "as"
# env = Env()
# env["asd"] = 5
# print(env["asd"])
# if a in env:
#     print("WORKS")
#
# if b in env:
#     print("WS")
#
# env["asd"] = 6
#
#
# print((1, env["asd"]))
# print((1,env))
