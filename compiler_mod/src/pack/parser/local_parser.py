
# local assignment in expr
from pack.ast import local_ast
from pack.ast.local_ast import *

import pack.parser.gen_helper as gen_helper


generator_local = local_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(local_ast.used_procedures_and_classes,generator_local)

def p_expression_local(p):
    'expression : local ID assign expression in expression'
    p[0] = generator_local.LocalExpression(p[2],p[4],p[6])

def p_expression_letrec(p):
    'expression : letrec ID assign expression in expression'
    p[0] = generator_local.LocalExpression(p[2],p[4],p[6])


generator_local = genHelperVar.set_generator_module_and_check(local_ast)
