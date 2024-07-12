


from src.ast import control_ast
from src.ast.control_ast import *

import src.parser.gen_helper as gen_helper


generator_control = control_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(control_ast.used_procedures_and_classes,generator_control)

def p_expression_if_then(p):
    '''expression : IF expression THEN expression
    '''
    p[0] = generator_control.IfThenExpression(p[2],p[4])
def p_expression_if_then_else(p):
    '''expression : IF expression THEN expression ELSE expression
    '''
    p[0] = generator_control.IfThenElseExpression(p[2],p[4],p[6])


def p_expression_loop_do_expr(p):
    '''expression : LOOP expression DO expression
    '''
    p[0] = generator_control.LoopDoExpression(p[2],p[4])

def p_expression_for_do_expr(p):
    '''expression : FOR expression ";" expression ";" expression DO expression
    '''
    p[0] = generator_control.ForDoExpression(p[2],p[4],p[6],p[8])

def p_expression_while_do_expr(p):
    '''expression : WHILE expression DO expression
    '''
    p[0] = generator_control.WhileExpression(p[2],p[4])   

generator_control = genHelperSequences.set_generator_module_and_check(control_ast)
