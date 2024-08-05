import numpy as np
from ..environment import Env
from ..Expression import InterpretedExpression, getAllClasses, ic

class FloatExpression(InterpretedExpression):
    def __init__(self, value):
        self.value=value

    def eval(self,env,is_struct=False):
         float_val = self.value
         return float(float_val), env 

class CharExpression(InterpretedExpression):
    def __init__(self, value):
        self.value=value

    def eval(self,env,is_struct=False):
        return self.value, env

class StringExpression(InterpretedExpression):
    def __init__(self, value):
        self.value=value

    def eval(self,env,is_struct=False):
        return str(self.value), env



class ArrayExpression(InterpretedExpression):
    def __init__(self, array_list):
        self.array_list=array_list

    def eval(self,env,is_struct=False):
        array_list =[self.array_list[i].eval(env,is_struct)[0] for i in range(len(self.array_list))]
        arr = np.array(array_list)
        return arr, env
        
class ArrayCallExpression(InterpretedExpression):
    def __init__(self, array_name,i):
        self.array_name=array_name
        self.i=i

    def eval(self,env,is_struct=False):
        # array_list =[self.array_name[i].eval(env,is_struct)[0] for i in range(len(self.array_name))]
        # arr = np.array(array_list)
        arr= env[self.array_name]
        return arr[self.i], env

def head(l):
    return l[0]

def tail(l):
    return l[1]

def array2list(a):
    return None if a==None or len(a)==0 else (a[0], ListExpression(a[1:]))

class ListExpression(InterpretedExpression):
    def __init__(self, lst):
        self.lst=array2list(lst)

    def eval(self,env,is_struct=False):
        if self.lst is not None:
            return (self.lst[0].eval(env,is_struct)[0],
                    self.lst[1].eval(env,is_struct)[0]),env
        return None, env



used_procedures_and_classes = getAllClasses()

