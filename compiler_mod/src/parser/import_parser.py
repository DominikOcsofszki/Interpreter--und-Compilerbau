

# local assignment in expr
from src.ast import import_ast
from src.ast.import_ast import *

from .. import gen_helper


generator_local = import_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(import_ast.used_procedures_and_classes,generator_local)

def p_expression_import_as(p):
    'expression : IMPORT ID AS ID'
    p[0] = generator_local.ImportAsExpression(p[2],p[4])

def p_expression_import(p):
    'expression : IMPORT ID'
    p[0] = generator_local.ImportExpression(p[2])

generator_local = genHelperVar.set_generator_module_and_check(import_ast)
