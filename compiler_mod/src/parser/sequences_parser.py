

from ..ast.sequences_ast import *


from ..Nodes import Node,Expr


def p_expression_sequence(p):
    'expression : "{" sequence "}" '
    p[0] = Node(Expr.SequenceExpression,p[2])

def p_expression_expressions(p):
    '''sequence :   sequence ";" expression 
                |   expression '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        p[0] = *p[1],p[3]

