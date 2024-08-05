#
from ..Expression import InterpretedExpression, getAllClasses,ic
from ..top_configs import EVAL_EXPR_BEFORE_SAVE_TO_TMP



class WriteIdExpression(InterpretedExpression):
    def __init__(self, id_always_as_string, value):
        self.id_string=id_always_as_string
        self.value=value

    # def eval(self,env,is_struct=False):
    def eval(self,env,is_struct=False):
        if is_struct:
            if isinstance(self.value, str) or isinstance(self.value, int):
                env.set_struct_dict_entry(self.id_string,  self.value)
                return self.value, env
            else:
                val = env.set_struct_dict_entry(self.id_string,  self.value.eval(env)[0])
                # val = self.value.eval(env,is_struct)[0]
                # find_env[self.id_string] = val
                ic("=============h6==================")
                ic("=============h6==================")
                ic(env)
                # exit()
                return val, env

            
        else:
            find_env = findEnvWithIdWrite(self.id_string,env)
        if isinstance(self.value, str) or isinstance(self.value, int):
            find_env[self.id_string] = self.value
            ic("=============h6==================")
            ic("=============h6==================")
            ic(find_env)
            return self.value, env
        else:
            val = self.value.eval(env,is_struct)[0]
            find_env[self.id_string] = val
            ic("=============h6==================")
            ic("=============h6==================")
            ic(find_env)
            return val, env

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

    def eval(self,env,is_struct=False):
        return env[self.id], env


class ReadParentIdExpression(InterpretedExpression):
    def __init__(self, id,dots):
        ic("=============h5==================")
        ic(self, id,dots)
        exit()
        self.id=id
        self.n_parents=dots-1

    def eval(self,env,is_struct=False):
        if self.n_parents == 0:
            return env[self.id], env
        else:
            for _ in range(self.n_parents):
                parent_struct =env["parent_in_struct"]
                # parent = env["parent"]
                if parent_struct:
                    return parent_struct(ReadIdExpression(self.id)), env
                    return parent.env[self.id], env
        return None, env


class WriteIdStructExpression(InterpretedExpression):
    def __init__(self, id_always_as_string, value):
        self.id_string=id_always_as_string
        self.value=value

    def eval(self,env,is_struct=False):
        find_env = findEnvWithIdWrite(self.id_string,env)
        if isinstance(self.value, str) or isinstance(self.value, int):
            find_env[self.id_string] = self.value
            return self.value, env
        else:
            find_env[self.id_string] = self.value.eval(env,is_struct)[0]
            return self.value.eval(env,is_struct)[0], env


used_procedures_and_classes = getAllClasses()


