

# local assignment in expr
from pack.ast import lambda_ast_class
from pack.ast.lambda_ast_class import *

import pack.parser.gen_helper as gen_helper


generator_local = lambda_ast_class if True else None 
genHelperVar = gen_helper.GeneratorHelper(lambda_ast_class.used_procedures_and_classes,generator_local)

def p_expression_lambda(p):
    'expression :  ID lambda expression'
    p[0] = generator_local.LambdaExpression(p[1],p[3])

generator_local = genHelperVar.set_generator_module_and_check(lambda_ast_class)
