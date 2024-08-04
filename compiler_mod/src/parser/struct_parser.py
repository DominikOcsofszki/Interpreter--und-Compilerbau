
from icecream import ic
from ..Nodes import Node,Expr

def p_expression__new_struct(p):
    'expression : STRUCT "{" sequence_struct "}" '
    p[0] = Node(Expr.StructExpression,[p[3]])

def p_expression_struct_extend(p):
    'expression : EXTEND ID "{" sequence_struct "}" '
    p[0] = Node(Expr.StructExtendExpression,[p[2],p[4]])

def p_expression_expressions_struct(p):
    '''sequence_struct :    struct_assign 
                      |     sequence_struct ";"  struct_assign 
                      '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [*p[1],p[3]]

def p_expression_assign_struct_write_id(p):
    '''struct_assign :    "."  ID ASSIGN expression
                    |     "."  ID ASSIGN lambda_expression
                    |     "."  ID ASSIGN lambda_expression_struct
    '''
    p[0] = Node(Expr.AssignInStructExpression,[p[2],p[4]])

def p_expression_lambda__in_struct(p):
    '''lambda_expression_struct :   LAMBDA_START LAMBDA dots expression
                        |           LAMBDA_START expression_list  LAMBDA dots expression
    '''
    if len(p) == 5:
        p[0] = Node(Expr.LambdaStructArgsExpression,[[], p[3], p[4]])
    if len(p) == 6:
        p[0] = Node(Expr.LambdaStructArgsExpression,[p[2],p[4], p[5]])

def p_expression_write_id(p):
    '''assign_expression :  ID ASSIGN expression
                       |    ID ASSIGN lambda_expression
       expression : assign_expression
    '''
    if len(p)== 4:
        p[0] = Node(Expr.WriteIdExpression,[p[1],p[3]])
        # p[0] = p[1],p[3]
    else:
        p[0]=p[1]
def p_expression_dots(p):
    '''dots :   "."
            |   "." dots
    '''
    if len(p) == 2:
        p[0] = 1 
    else: 
        p[0] = p[2] +1

def p_expression_dot_outside(p):
    '''expression : ID dots ID'''
    if len(p)==4:
        p[0] = Node(Expr.StructVariableFromOutside,[p[1],p[2],p[3]])
    else:
        raise AssertionError("sth wrong in p_expression_dot_outside",p)

def p_expression_dot_outside_call(p):
    '''expression : ID dots ID "(" ")"
                |   ID dots ID "(" expression_list ")"
    '''
    if len(p)==6:
        p[0] = Node(Expr.StructCallFunctionFromOutside,[p[1],p[2],p[3],[]])
    else:
        p[0] = Node(Expr.StructCallFunctionFromOutside,[p[1],p[2],p[3],p[5]])


def p_expression_unary_operators_not(p):
    '''expression : NOT expression 
    '''
    p[0] = Node(Expr.NotBoolExpression,[p[2]])




def p_expression_lambda__outside(p):
    '''lambda_expression :      LAMBDA_START LAMBDA expression
                    |           LAMBDA_START expression_list  LAMBDA expression
        expression : lambda_expression
    '''
    if len(p) == 4:
        p[0] = Node(Expr.LambdaArgsExpression,[[], p[3]])
    if len(p) == 5:
        p[0] = Node(Expr.LambdaArgsExpression,[p[2], p[4]])
    if len(p) == 2:
        p[0] = p[1]

