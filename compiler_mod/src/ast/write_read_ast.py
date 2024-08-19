#
from ..Expression import InterpretedExpression, getAllClasses, ic
from ..symbol_table import SYMBOL_TABLE
from ..top_configs import EVAL_EXPR_BEFORE_SAVE_TO_TMP


class WriteIdExpression(InterpretedExpression):
    def __init__(self, id_always_as_string, value, var_info_symbol=None):
        # ic(self, id_always_as_string, value)
        self.id_string = id_always_as_string
        self.value = value
        self.var_info_symbol = var_info_symbol

    def eval(self, env):
        var_info_symbol = self.var_info_symbol #= {"line" : 0, "col" : 10}
        # ic("=============h14==================")
        # ic(env.level)
        if not env.env_name == "ENV_GLOBAL":
            find_env = findEnvWithIdWrite(self.id_string, env)
        else:
            find_env = env
        # ic(env.level)
        # ic(">>>", find_env.level)
        # SYMBOL_TABLE.ad

        if isinstance(self.value, str) or isinstance(self.value, int):
            find_env.set_item_with_infos(self.id_string, self.value, var_info_symbol)
            # find_env[self.id_string] = self.value
            return self.value, env
        else:
            find_env.set_item_with_infos(self.id_string, self.value.eval(env)[0], var_info_symbol)
            # find_env[self.id_string] = self.value.eval(env)[0]
            return self.value.eval(env)[0], env


def findEnvWithIdWrite(id, env):
    # if env.env_name == "ENV_GLOBAL":
    # # if env.parent.env_name == "ENV_IMPORTS":
    #         return env
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
        self.id = id

    def eval(self, env):
        return env[self.id], env


class ReadParentIdExpression(InterpretedExpression):
    def __init__(self, id, dots):
        ic(self, id, dots)
        exit()
        self.id = id
        self.n_parents = dots - 1

    def eval(self, env):
        if self.n_parents == 0:
            return env[self.id], env
        else:
            for _ in range(self.n_parents):
                parent_struct = env["parent_in_struct"]
                # parent = env["parent"]
                if parent_struct:
                    return parent_struct(ReadIdExpression(self.id)), env
                    # return parent.env[self.id], env
        return None, env


class WriteIdStructExpression(InterpretedExpression):
    def __init__(self, id_always_as_string, value):
        self.id_string = id_always_as_string
        self.value = value

    def eval(self, env):
        if not env.env_name == "ENV_GLOBAL":
            find_env = findEnvWithIdWrite(self.id_string, env)
        else:
            find_env = env

        # find_env = findEnvWithIdWrite(self.id_string,env)
        if isinstance(self.value, str) or isinstance(self.value, int):
            find_env[self.id_string] = self.value
            return self.value, env
        else:
            find_env[self.id_string] = self.value.eval(env)[0]
            return self.value.eval(env)[0], env


used_procedures_and_classes = getAllClasses()
