
from icecream import ic
from ..Nodes import Node,Expr

def p_expression__new_struct(p):
    'expression : STRUCT "{" sequence_struct "}" '
    p[0] = Node(Expr.StructExpression,[p[3]])
    ic(p[3])

def p_expression_struct_extend(p):
    'expression : EXTEND ID "{" sequence_struct "}" '
    p[0] = Node(Expr.StructExtendExpression,[p[2],p[4]])

def p_expression_expressions_struct(p):
    '''sequence_struct :    seq_struct_assign_expression 
                      |     sequence_struct ";"  seq_struct_assign_expression 
                      '''
    if len(p) == 2:
        p[0] = [p[1]]
    else:
        p[0] = [*p[1],p[3]]
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

# def p_expression_dot_struct(p):
#     '''dots_in_struct_expression : dots ID
#     '''
#     p[0] = [ [],p[1],p[2] ]

# def p_expression_struct_use_parent_WORKING(p):
#     '''expression : dots_in_struct_expression "(" ")"
#                 |   dots_in_struct_expression "(" expression_list ")"
#
#     '''
#     if len(p) == 4:
#         p[0] = Node(Expr.StructInsideArgsExpression,[p[1],[]])
#     if len(p) == 5:
#         p[0] = Node(Expr.StructInsideArgsExpression,[p[1],p[3]])

def p_expression_unary_operators_not(p):
    '''expression : NOT expression 
    '''
    p[0] = Node(Expr.NotBoolExpression,[p[2]])

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


# def p_expression_write_id_dots(p):
#     'expression : assign_expression'
#     # 'expression : dots ID ASSIGN expression'
#     p[0] = Node(Expr.WriteIdExpression,[p[2],p[4]])

def p_expression_assign(p):
    '''seq_struct_assign_expression : '.' assign_expression 
     '''
    # '''seq_assign_expression : dots ID ASSIGN expression '''
    # p[0] = Node(Expr.WriteIdStructExpression,[p[2],p[4]])
    p[0] = Node(Expr.WriteIdStructExpression,[*p[2]])
# def p_expression_assign(p):
#     '''seq_struct_assign_expression : '.' ID ASSIGN expression 
#                                     | '.' ID ASSIGN lambda_expression '''
#     # '''seq_assign_expression : dots ID ASSIGN expression '''
#     p[0] = Node(Expr.WriteIdStructExpression,[p[2],p[4]])
#     ic(p[0].children)


def p_expression_lambda__in_struct(p):
    '''lambda_expression :      LAMBDA_START expression_list  LAMBDA seq_struct_assign_expression
                    |           LAMBDA_START LAMBDA seq_struct_assign_expression
    '''
    if len(p) == 4:
        p[0] = Node(Expr.LambdaArgsExpression,[[], p[3]])
    if len(p) == 5:
        p[0] = Node(Expr.LambdaArgsExpression,[p[2], p[4]])
    ic("=============h22==================")
    ic(p[0])

def p_expression_lambda__outisde(p):
    '''lambda_expression :      LAMBDA_START LAMBDA expression
                    |           LAMBDA_START expression_list  LAMBDA expression
    '''
    if len(p) == 4:
        p[0] = Node(Expr.LambdaArgsExpression,[[], p[3]])
    if len(p) == 5:
        p[0] = Node(Expr.LambdaArgsExpression,[p[2], p[4]])
    ic("=============h24==================")
    ic(p[0])


# def p_expression_lambd(p):
#    '''expression : lambda_expression'''
#    p[0] = p[1]





















