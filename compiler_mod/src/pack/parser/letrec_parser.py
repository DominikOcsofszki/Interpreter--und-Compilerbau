

# local assignment in expr
from pack.ast import letrec_ast
from pack.ast.letrec_ast import *

import pack.parser.gen_helper as gen_helper


generator_local = letrec_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(letrec_ast.used_procedures_and_classes,generator_local)

def p_expression_letrec(p):
    'expression : letrec ID assign expression lambda expression'
    ic(p)
    p[0] = generator_local.LetrecExpression(p[2],p[4],p[6])
    ic(p[0])
generator_local = genHelperVar.set_generator_module_and_check(letrec_ast)
