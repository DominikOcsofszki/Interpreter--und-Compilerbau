import copy

from numpy import append
from .top_configs import SHOW_ENV_IMPORTS
from icecream import ic
all_envs=[]
class Env:

    def __init__(self,parent=None,env_name=None) -> None:
        self.parent = parent
        self.env_dict={}
        self.struct_dict={}
        self.env_name=env_name
        global all_envs
        all_envs.append(self)

    def __contains__(self,key):
        if key in self.env_dict:
            return True
        elif self.parent:
            return key in self.parent
        return False

    def deep_copy(self):
        return copy.deepcopy(self)

    def deep_copy__only_env(self):
        return copy.deepcopy(self.env_dict)

    def deep_copy_struct_dict(self):
        return copy.deepcopy(self.struct_dict)


# //TODO!!!
    def __repr__(self) -> str:
        if self.parent:
            if self.parent.parent:
                return str(self.env_dict)+"\n" + str(self.parent )
            else:
                if SHOW_ENV_IMPORTS:
                    return str(self.env_dict)+ "\n\nIMPORTS: " + str(self.parent)
                return str(self.env_dict)

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

    def get_struct_dict_entry(self,key):
        # ic(self,key)
        ic("=====get_struct_dict_entry========h20==================")
        if key in self.struct_dict:
            return self.struct_dict[key]
        elif self.parent and len(self.parent.struct_env_dict) == 0:
            return self.parent[key]
        return None
    def set_struct_dict_entry(self,key,entry):
        # ic(self,key,entry)
        ic("=============h21==set_struct_dict_entry================")
        self.struct_dict[key] = entry
    # def print_all_envs(self):
    #     ic("==>print all print_all_envs====================")
    #     for new_env in all_envs:
    #         ic("=============h==================")
    #         ic(new_env.env_name, new_env, new_env.struct_dict)
    #     ic("print all print_all_envs<======================")
