from ..Nodes import Node,Literals
from ..Nodes import Expr
def p_expr_uminus(p):
    'expression : "-" expression %prec UMINUS'
    p[0] = -p[2]

def p_expression_num(p):
    'expression : NUMBER'
    p[0] = Literals(Expr.NumberExpression,p[1])


def p_expression_bool(p):
    ''' expression : BOOL'''
    p[0] = Literals(Expr.BoolValueExpression,p[1])

def p_expression_types_float(p):
    'expression : FLOAT'
    p[0] = Literals(Expr.FloatExpression,p[1])

def p_expression_types_string(p):
    'expression : STRING '
    p[0] = Literals(Expr.StringExpression,p[1])

def p_expression_types_char(p):
    'expression : CHAR '
    p[0] = Literals(Expr.CharExpression,p[1])


def p_expression_read_id(p):
    'expression : ID'
    p[0] = Literals(Expr.ReadIdExpression,p[1])





# Move other place?


def p_expression_unary_operators_not(p):
    '''expression : NOT expression
    '''
    p[0] = Node(Expr.NotBoolExpression,[p[2]])

def p_expression_read_parent_id(p):
    'expression :  dots ID'
    p[0] = Node(Expr.ReadParentIdExpression,[p[2],p[1]])

def p_expression_write_id(p):
    'expression : ID ASSIGN expression'
    p[0] = Node(Expr.WriteIdExpression,[p[1],p[3]])

def p_expression_write_id_dots(p):
    'expression : dots ID ASSIGN expression'
    p[0] = Node(Expr.WriteIdExpression,[p[2],p[4]])



