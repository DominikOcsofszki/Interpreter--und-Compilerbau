
from pack.ast import local_ast_class
from pack.ast.local_ast_class import *

import pack.parser.gen_helper as gen_helper


generator_local = local_ast_class if True else None 
genHelperVar = gen_helper.GeneratorHelper(local_ast_class.used_procedures_and_classes,generator_local)

def p_expression_types(p):
    'expression : float'
    p[0] = generator_local.FloatExpression(p[2])

generator_local = genHelperVar.set_generator_module_and_check(local_ast_class)
