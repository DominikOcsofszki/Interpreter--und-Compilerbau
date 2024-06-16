


from pack.ast import control_ast
from pack.ast.control_ast import *

import pack.parser.gen_helper as gen_helper


generator_control = control_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(control_ast.used_procedures_and_classes,generator_control)

# loop expr do expr
# for assign;bool_expr;assign do expr
# for assign;bool_expr;assign do lock var expr << optional
# ===================================================
# if bool_expr then expr
# if bool_expr then expr else expr

def p_expression_if_then(p):
    '''expression : if expression then expression
    '''
    p[0] = generator_control.IfThenExpression(p[2],p[4])
def p_expression_if_then_else(p):
    '''expression : if expression then expression else expression
    '''
    p[0] = generator_control.IfThenElseExpression(p[2],p[4],p[6])
    ic(p[0])


def p_expression_loop_do_expr(p):
    '''expression : loop expression do expression
    '''
    p[0] = generator_control.LoopDoExpression(p[2],p[4])
# def p_expression_expressions(p):
#     '''sequence :   sequence ";" expression
#                 |   expression
#     '''
#     p[0] = [p[1]] if len(p) == 2 else [*p[1],p[3]]
#     # p[0] = generator_sequences.ExpressionsExpression(p[1],p[3])

def p_expression_for_do_expr(p):
    '''expression : for expression ";" expression ";" expression do expression
    '''
    p[0] = generator_control.ForDoExpression(p[2],p[4],p[6],p[8])

def p_expression_while_do_expr(p):
    '''expression : while expression do expression
    '''
    p[0] = generator_control.WhileExpression(p[2],p[4])   

generator_control = genHelperSequences.set_generator_module_and_check(control_ast)
