

# local assignment in expr
from pack.ast import types_ast
from pack.ast.types_ast import *

import pack.parser.gen_helper as gen_helper


generator_local = types_ast if True else None 
genHelperVar = gen_helper.GeneratorHelper(types_ast.used_procedures_and_classes,generator_local)

def p_expression_letrec(p):
    'expression : letrec ID assign expression lambda expression'
    p[0] = generator_local.LetrecExpression(p[2],p[4],p[6])
generator_local = genHelperVar.set_generator_module_and_check(types_ast)
