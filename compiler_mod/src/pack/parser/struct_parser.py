


from pack.ast import struct_ast
from pack.ast import var_ast
from pack.ast.struct_ast import *
from pack.ast.var_ast import *

import pack.parser.gen_helper as gen_helper


generator_sequences = struct_ast if True else None 
generator_vars = var_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(struct_ast.used_procedures_and_classes,generator_sequences)


def p_expression_struct(p):
    'expression : struct "{" sequence "}" '
    p[0] = generator_sequences.StructExpression(p[3])

def p_expression_struct_use(p):
    'expression : ID "." ID '
    p[0] = generator_sequences.StructCallExpression(generator_vars.ReadIdExpression(p[1]),generator_vars.ReadIdExpression(p[3]))

def p_expression_struct_extend(p):
    'expression : extend struct "{" sequence "}" '
    ic(p[2])
    ic(p[4])
    p[0] = generator_sequences.StructExtendExpression(p[2],p[4])


generator_sequences = genHelperSequences.set_generator_module_and_check(struct_ast)
