
from icecream import ic
from ..Nodes import Node,Expr

def p_expression__new_struct(p):
    'expression : STRUCT "{" sequence_struct "}" '
    p[0] = Node(Expr.StructExpression,[p[3]])

def p_expression_struct_extend(p):
    'expression : EXTEND ID "{" sequence_struct "}" '
    p[0] = Node(Expr.StructExtendExpression,[p[2],p[4]])

def p_expression_dots(p):
    '''dots :    "."
        |       "." dots
    '''
    if len(p) == 2:
        p[0] = 1 
    else: 
        p[0] = p[2] +1


def p_expression_dot_struct(p):
    '''dot_expression : dots ID
                    |   ID dots ID
    '''
    if len(p) == 3:
        p[0] = [ [],p[1],p[2] ]
    else:
        p[0] = [ p[1],p[2],p[3] ] 

def p_expression_struct_use_parent_WORKING(p):
    '''expression : dot_expression                 
                |   dot_expression "(" ")"
                |   dot_expression "(" expression_list ")"

    '''
    if len(p)==2:
        p[0] = Node(Expr.StructCallNParentFunctionExpression,[p[1],None])
    if len(p) == 4:
        p[0] = Node(Expr.StructCallNParentFunctionExpression,[p[1],[]])
    if len(p) == 5:
        p[0] = Node(Expr.StructCallNParentFunctionExpression,[p[1],p[3]])

def p_expression_unary_operators_not(p):
    '''expression : NOT expression '''
    p[0] = Node(Expr.NotBoolExpression,[p[2]])

def p_expression_write_id(p):
    'expression : ID ASSIGN expression'
    p[0] = Node(Expr.WriteIdExpression,[p[1],p[3]])

#Delete ok?
# def p_expression_write_id_dots(p):
#     'expression : dots ID ASSIGN expression'
#     p[0] = Node(Expr.WriteIdStructExpression,[p[2],p[4]])

def p_expression_assign(p):
    '''seq_assign_expression : dots ID ASSIGN expression '''
    p[0] = Node(Expr.WriteIdStructExpression,[p[2],p[4]])

def p_expression_expressions_struct(p):
    '''sequence_struct :    seq_assign_expression 
                      |     sequence_struct ";"  seq_assign_expression 
                      '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [*p[1],p[3]]
























