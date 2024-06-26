
class InterpretedExpression:
    def eval(self,env):
        raise Exception('eval not impl')

def getAllClasses():
    import inspect, sys
    classes = [name for name, obj in inspect.getmembers(sys.modules[__name__], inspect.isclass) 
              if obj.__module__ is __name__]
    classes_cleaned = [ clazz for clazz in classes if clazz != "InterpretedExpression" ]
    return classes_cleaned


