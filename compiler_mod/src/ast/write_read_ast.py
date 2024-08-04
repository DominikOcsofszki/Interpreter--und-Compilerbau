#
from copy import Error
from ..Expression import InterpretedExpression, getAllClasses,ic
from ..top_configs import EVAL_EXPR_BEFORE_SAVE_TO_TMP



class WriteIdExpression(InterpretedExpression):
    def __init__(self, id_always_as_string, value):
        self.id_string=id_always_as_string
        self.value=value

    def eval(self,env,is_struct=False):
        ic("=============h40==================")
        if is_struct:
            ic("================>is inside struct<<<<<<<<<<<<<<<<<<")
            ic("=============h45==================")
            ic(env)
            ic(self.value.eval(env,is_struct=True)[0])
            ic(self.value.children)
            # env.struct_dict[self.id_string] = self.value.eval(env)[0]
            # ic(env.struct_dict[self.id_string])
            # ic("=============h41==================")
            find_env = env
            # find_env = env.struct_dict
            # ic(find_env)
            ic("=============h42==================")
            # exit()
        else:
            find_env = findEnvWithIdWrite(self.id_string,env)
        if isinstance(self.value, str) or isinstance(self.value, int):
            find_env[self.id_string] = self.value
            ic(find_env)
            return self.value, env
        else:
            find_env[self.id_string] = self.value.eval(env)[0]
            ic(find_env)
            return self.value.eval(env)[0], env

def findEnvWithIdWrite(id,env):
    if env.parent.env_name == "ENV_IMPORTS":
            return env
    parent_env = env
    item = parent_env.env_dict.get(id)
    last_parent = parent_env
    while parent_env and not item:
        last_parent = parent_env
        item = parent_env.env_dict.get(id)
        if item:
            return last_parent
        parent_env = parent_env.parent
    return env


class ReadIdExpression(InterpretedExpression):
    def __init__(self, id):
        self.id=id

    def eval(self,env):
        return env[self.id], env

used_procedures_and_classes = getAllClasses()


