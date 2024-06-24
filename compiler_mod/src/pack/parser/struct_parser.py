


from pack.ast import struct_ast
from pack.ast import var_ast
from pack.ast.struct_ast import *
from pack.ast.var_ast import *

import pack.parser.gen_helper as gen_helper


gen = struct_ast if True else None 
generator_vars = var_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(struct_ast.used_procedures_and_classes,gen)

P_line=0

def p_expression_struct(p):
    'expression : struct "{" sequence "}" '
    p[0] = gen.StructExpression(p[3])

# def p_expression_struct_use(p):
#     'expression : ID "." ID '
#     # p[0] = generator_sequences.StructCallExpression(p[1],p[3])
#     p[0] = generator_sequences.StructCallExpression(generator_vars.ReadIdExpression(p[1]),generator_vars.ReadIdExpression(p[3]))

# def p_expression_struct_use_fn(p):
#     '''expression :     ID "." ID "(" id_list ")"
#                     |   ID "." ID "(" ")"
#  
#     '''
#     P_line = p.lineno(1)
#     p[0] = gen.StructCallFunExpression(
#                 generator_vars.ReadIdExpression(p[1]),
#                 generator_vars.ReadIdExpression(p[3]),
#                 [x for x in p[5] if len(p) == 6],
            # )
    # p[0] = generator_sequences.StructCallFunExpression(generator_vars.ReadIdExpression(p[1]),p[3])

def p_expression_struct_extend(p):
    'expression : extend ID "{" sequence "}" '
    p[0] = gen.StructExtendExpression(p[2],p[4])

def p_expression_dot_struct(p):
    '''dot_expression : ID "." ID
                | ID "." "." ID 
                | ID "." "." "." ID 
                | ID "." "." "." "." ID 
                | ID "." "." "." "." "." ID 
                | ID "." "." "." "." "." "." ID 
    '''
    p[0]= [p[1],p[len(p)-1],len(p)-3]


def p_expression_struct_use_parent_WORKING(p):
    '''expression : dot_expression
                |   dot_expression "(" ")"
                |   dot_expression "(" id_list ")"

    '''
    ic(p[1])
    if len(p) == 2:
        p[0] = gen.StructCallNParentWithFunExpression(p[1],None)
        # p[0] = gen.StructCallNParentExpression(*p[1])
    if len(p) == 4:
        p[0] = gen.StructCallNParentWithFunExpression(p[1],[])
    if len(p) == 5:
        p[0] = gen.StructCallNParentWithFunExpression(p[1],p[3])





# def p_expression_struct_use_parent(p):
#     '''expression : ID "." ID "(" ")"
#                 | ID "." "." ID "(" ")" 
#                 | ID "." "." "." ID  "(" ")"
#                 | ID "." "." "." "." ID "(" ")"
#                 | ID "." "." "." "." "." ID "(" ")"
#                 | ID "." "." "." "." "." "." ID "(" ")"
#
#     '''
#     p[0]=gen.StructCallNParentExpression(
#             generator_vars.ReadIdExpression(p[1]),
#             p[len(p)-1-2],
#             (len(p)-1-3-2)
#             )

# def p_expression_call_no_vars_struct(p):
#     'fn :  ID "(" ")"'
#     p[0] = gen.CallExpression(p[1],[])
#
# def p_expression_call_args_struct(p):
#     'fn :  ID "(" id_list ")"'
#     p[0] = gen.CallExpression(p[1],[*p[3]])

gen = genHelperSequences.set_generator_module_and_check(struct_ast)
