
from src.ast import local_ast
from src.ast.local_ast import *

import src.parser.gen_helper as gen_helper


generator_local = local_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(local_ast.used_procedures_and_classes,generator_local)

def p_expression_local(p):
    'expression : LOCAL ID ASSIGN expression IN expression'
    p[0] = generator_local.LocalExpression(p[2],p[4],p[6])


generator_local = genHelperVar.set_generator_module_and_check(local_ast)
