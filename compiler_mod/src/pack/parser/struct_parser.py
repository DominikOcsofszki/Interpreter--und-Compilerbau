
from pack.ast import struct_ast
from pack.ast import write_read_ast
from pack.ast.struct_ast import *
from pack.ast.write_read_ast import *

import pack.parser.gen_helper as gen_helper


gen = struct_ast if True else None 
generator_vars = write_read_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(struct_ast.used_procedures_and_classes,gen)

def p_expression_expressions_struct(p):
    '''sequence_struct :   sequence_struct ";" "." ID ASSIGN expression 
                        |  "." ID ASSIGN expression 
                        '''
    # p[0] = [generator_vars.WriteIdExpression(p[1],p[3])] if len(p) == 4 else [*p[1],generator_vars.WriteIdExpression(p[3],p[5])]
    p[0] = [generator_vars.WriteIdExpression(p[2],p[4])] if len(p) == 5 else [*p[1],generator_vars.WriteIdExpression(p[4],p[6])]

def p_expression__new_struct(p):
    'expression : STRUCT "{" sequence_struct "}" '
    p[0] = gen.StructExpression(p[3])

def p_expression_struct_extend(p):
    'expression : EXTEND ID "{" sequence_struct "}" '
    p[0] = gen.StructExtendExpression(p[2],p[4])

def p_expression_dots(p):
    '''dots :    "."
        |       "." dots
    '''
    p[0] = 1 if len(p) == 2 else p[2] +1

def p_expression_dot_struct(p):
    '''dot_expression : ID dots ID
                    |   dots ID
    '''
    p[0]= [p[1],p[3],p[2]] if len(p)==4 else [[],p[2],p[1]]

def p_expression_struct_use_parent_WORKING(p):
    '''expression : dot_expression
                |   dot_expression "(" ")"
                |   dot_expression "(" expression_list ")"

    '''
    if len(p) == 2:
        p[0] = gen.StructCallNParentWithFunExpression(p[1],None)
    if len(p) == 4:
        p[0] = gen.StructCallNParentWithFunExpression(p[1],[])
    if len(p) == 5:
        p[0] = gen.StructCallNParentWithFunExpression(p[1],p[3])

gen = genHelperSequences.set_generator_module_and_check(struct_ast)
