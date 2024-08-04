from icecream import ic
from .environment import Env

from . import top_configs as top_config
class InterpretedExpression:

    # def eval(self,env:Env,node_info=None):
    #     if node_info:
    #         ic(node_info)
    def eval(self,env:Env,is_struct=False):
        # raise NotImplementedError("Child of InterpretedExpression not impl")
        # return is_struct
        return None, env


    def __repr__(self) -> str:
        class_name = type(self).__name__
        if top_config.PRINT_1_ONLY_ATTRIBUTES:
            attributes = [attr for attr in dir(self) 
                          if not attr.startswith('__') and not attr.startswith("eval")]
            return str(attributes)
        if top_config.PRINT_2_DEBUD_MODE:
            # attrs = vars(self)
            # eachh = [item for item in attrs.items()]
            # return str(eachh)

            return "<"+class_name+">\n" + str(vars(self)) + "\n"
        return "<"+class_name+">\n"
        return  str(self.__class__)



def getAllClasses():
    import inspect, sys
    classes = [name for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) 
              if obj.__module__ is __name__]
    classes_cleaned = [ clazz for clazz in classes if clazz != "InterpretedExpression" ]
    return classes_cleaned


