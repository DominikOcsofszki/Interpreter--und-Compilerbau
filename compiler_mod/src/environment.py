from os import error
import copy
from top_configs import SHOW_ENV_IMPORTS
# from pack.ast.var_ast import ReadIdExpression,WriteIdExpression

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

    def deep_copy(self):
        return copy.deepcopy(self)


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

