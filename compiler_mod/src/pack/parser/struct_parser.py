


from pack.ast import struct_ast
from pack.ast import var_ast
from pack.ast.struct_ast import *
from pack.ast.var_ast import *

import pack.parser.gen_helper as gen_helper


generator_sequences = struct_ast if True else None 
generator_vars = var_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(struct_ast.used_procedures_and_classes,generator_sequences)

P_line=0

def p_expression_struct(p):
    'expression : struct "{" sequence "}" '
    p[0] = generator_sequences.StructExpression(p[3])

# def p_expression_struct_use(p):
#     'expression : ID "." ID '
#     # p[0] = generator_sequences.StructCallExpression(p[1],p[3])
#     p[0] = generator_sequences.StructCallExpression(generator_vars.ReadIdExpression(p[1]),generator_vars.ReadIdExpression(p[3]))

def p_expression_struct_use_fn(p):
    '''expression :     ID "." ID "(" id_list ")"
                    |   ID "." ID "(" ")"
 
    '''
    P_line = p.lineno(1)
    p[0] = generator_sequences.StructCallFunExpression(
                generator_vars.ReadIdExpression(p[1]),
                generator_vars.ReadIdExpression(p[3]),
                [x for x in p[5] if len(p) == 6],
            )
    # p[0] = generator_sequences.StructCallFunExpression(generator_vars.ReadIdExpression(p[1]),p[3])

def p_expression_struct_extend(p):
    'expression : extend ID "{" sequence "}" '
    p[0] = generator_sequences.StructExtendExpression(p[2],p[4])

def p_expression_struct_use_parent(p):
    '''expression : ID "." ID 
                | ID "." "." ID 
                | ID "." "." "." ID 
                | ID "." "." "." "." ID 
                | ID "." "." "." "." "." ID 
                | ID "." "." "." "." "." "." ID 

    '''
    p[0]=generator_sequences.StructCallNParentExpression(
            generator_vars.ReadIdExpression(p[1]),
            generator_vars.ReadIdExpression(p[len(p)-1]),
            (len(p)-1-3)
            )


generator_sequences = genHelperSequences.set_generator_module_and_check(struct_ast)
