


from pack.ast import struct_ast
from pack.ast.struct_ast import *

import pack.parser.gen_helper as gen_helper


generator_sequences = struct_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(struct_ast.used_procedures_and_classes,generator_sequences)


def p_expression_struct(p):
    'expression : struct "{" sequence "}" '
    p[0] = generator_sequences.StructExpression(p[3])

def p_expression_struct_use(p):
    'expression : ID "." ID '
    p[0] = generator_sequences.StructCallExpression(p[1],p[3])

generator_sequences = genHelperSequences.set_generator_module_and_check(struct_ast)
