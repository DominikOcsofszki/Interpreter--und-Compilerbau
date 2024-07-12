

from ..ast.sequences_ast import *


from ..Nodes import Node,Expr


def p_expression_sequence(p):
    'expression : "{" sequence "}" '
    # p[0] = Node(Expr.SequenceExpression,p[2])
    p[0] = Node(Expr.SequenceExpression,[p[2]])
    # ic([Node(x) for x in p[2]])

def p_expression_expressions(p):
    '''sequence :   expression 
                |   sequence ";" expression '''
    if len(p) == 2:
        p[0] = p[1]
    else:
        if type(p[1]) != Node:
            ic("=============================")
            ic(*p[1])
            ic(type(p[1]))
            ic(len(p[1]))
            p[0] = [*p[1],p[3]]

        else:
            p[0] = [p[1],p[3]]
#
            # p[0] = p[1],p[3]


