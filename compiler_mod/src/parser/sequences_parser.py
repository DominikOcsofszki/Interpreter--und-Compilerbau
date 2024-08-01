

from ..ast.sequences_ast import *


from ..Nodes import Node,Expr


def p_expression_sequence(p):
    'expression : "{" sequence "}" '
    # p[0] = Node(Expr.SequenceExpression,p[2])
    p[0] = Node(Expr.SequenceExpression,[p[2]])
    # p[0] = Node("sequence",[p[2]])

def p_expression_seq_expr(p):
    '''sequence :   expression 
                |   sequence ";" expression '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        if type(p[1]) != Node:
            p[0] = [*p[1],p[3]]

        else:
            p[0] = [p[1],p[3]]
#
            # p[0] = p[1],p[3]


