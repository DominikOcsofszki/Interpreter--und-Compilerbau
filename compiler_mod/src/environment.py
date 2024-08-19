from os import error
import copy
from .top_configs import SHOW_ENV_IMPORTS
from icecream import ic

from .symbol_table import SYMBOL_TABLE


class Env:

    def __init__(self, parent=None, env_name=None) -> None:
        self.parent = parent
        self.env_dict = {}
        self.struct_dict = {}
        self.env_name = env_name
        self.level = self.calculate_level()
        # ic(self.level)

    def set_parent_env(self, parent):
        self.parent = parent
        self.level = self.calculate_level()

    def calculate_level(self) -> int:
        if self.env_name == "ENV_GLOBAL" or self.env_name == "ENV_IMPORTS":
            return 0
        else:
            return self.parent.level + 1

    def __contains__(self, key):
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
                return str(self.env_dict)+"\n" + str(self.parent)
            else:
                if SHOW_ENV_IMPORTS:
                    return str(self.env_dict) + "\n\nIMPORTS: " + str(self.parent)
                return str(self.env_dict)

        return str(self.env_dict)

    def __getitem__(self, key):
        # if type(key) is int: #or key.isdigit():
        #     return int(key)
        if key in self.env_dict:
            return self.env_dict[key]
        elif self.parent:
            return self.parent[key]
        return None

    # def set_local_var(self, var_name, var_info,index_from_env):
    #     self.tables[index_from_env][var_name] = var_info
    #
    def set_item_with_infos(self,key,value,var_info_symbol):
        self.env_dict[key] = value

        var_info = var_info_symbol
        if self.env_name != "ENV_IMPORTS":
            SYMBOL_TABLE.set_local_var(key, var_info, self.level)
            # ic(SYMBOL_TABLE)
            ic(key,SYMBOL_TABLE.get_local_var(key,self.level))
            # ic("=============h13==================")


    def __setitem__(self, key, value):
        self.env_dict[key] = value

        # var_info = {"val":value}
        # if self.env_name != "ENV_IMPORTS":
        #     SYMBOL_TABLE.set_local_var(key, var_info, self.level)
        #     # ic(SYMBOL_TABLE)
        #     ic(key,SYMBOL_TABLE.get_local_var(key,self.level))
        #     # ic("=============h13==================")

        # self.env_dict[key] = value

    # def get_struct_dict_entry(self,key):
    #     # ic(self,key)
    #     ic("=====get_struct_dict_entry========h20==================")
    #     if key in self.struct_dict:
    #         return self.struct_dict[key]
    #     elif self.parent and len(self.parent.struct_env_dict) == 0:
    #         return self.parent[key]
    #     return None
    # def set_struct_dict_entry(self,key,entry):
    #     # ic(self,key,entry)
    #     ic("=============h21==set_struct_dict_entry================")
    #     self.struct_dict[key] = entry
    #     self.struct_dict[key] = entry
    #     ic("=============h21==set_struct_dict_entry================")
    #     self.struct_dict[key] = entry
    #     self.struct_dict[key] = entry
