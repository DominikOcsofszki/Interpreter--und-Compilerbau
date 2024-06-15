
# local assignment in expr

from environment import Env
from pack.ast.Expression import InterpretedExpression, getAllClasses

class ImportAsExpression(InterpretedExpression):
    def __init__(self, import_name, new_name):
        self.import_name=import_name
        self.new_name=new_name

    def eval(self,env):
        print(env)
        env[self.new_name] =__import__(self.import_name)
        return None, env

class ImportExpression(InterpretedExpression):
    def __init__(self, import_name):
        self.import_name=import_name

    def eval(self,env):
        print(env)
        env[self.import_name] =__import__(self.import_name)
        return None, env


used_procedures_and_classes = getAllClasses()

