from src.lexer.literals_lexer import *

from ..Nodes import Node,Expr

def p_expression_binary_operators_arith(p):
    '''expression :   expression "+" expression
                    | expression "-" expression
                    | expression '*' expression
                    | expression '/' expression
    '''
    match p[2]:
        case "+"   : p[0] = Node(Expr.PlusExpression,[p[1],p[3]]) 
        case "-"   : p[0] = Node(Expr.MinusExpression,[p[1],p[3]]) 
        case "*"   : p[0] = Node(Expr.TimesExpression,[p[1],p[3]]) 
        case "/"   : p[0] = Node(Expr.DivideExpression,[p[1],p[3]]) 
        case _ : print("STH WROMG")


def p_expression_binary_operators_bool(p):
    '''expression :   expression AND expression
                    | expression EQ expression
                    | expression '=' expression
                    | expression '>' expression
                    | expression '<' expression
                    | expression GE expression
                    | expression LE expression
                    | expression NEQS expression
                    | expression OR expression
                    | expression NAND expression
    '''
    lowerp2 = p[2].lower()
    match lowerp2:
        case "and"      : p[0] = Node(Expr.AndExpression,[p[1],p[3]]) 
        case "eqcomp"   : p[0] = Node(Expr.EqCompExpression,[p[1],p[3]]) 
        case "="        : p[0] = Node(Expr.EqExpression,[p[1],p[3]]) 
        case ">="       : p[0] = Node(Expr.GeExpression,[p[1],p[3]]) 
        case ">"        : p[0] = Node(Expr.GtExpression,[p[1],p[3]]) 
        case "<="       : p[0] = Node(Expr.LeExpression,[p[1],p[3]]) 
        case "!="       : p[0] = Node(Expr.NotEqCompExpression,[p[1],p[3]]) 
        case "<"        : p[0] = Node(Expr.LtExpression,[p[1],p[3]]) 
        case "or"       : p[0] = Node(Expr.OrExpression,[p[1],p[3]]) 
        case "nand"     : p[0] = Node(Expr.NandExpression,[p[1],p[3]]) 




def p_expression_types_array(p):
    'expression : "[" expression_list "]"'
    p[0]=Node(Expr.ArrayExpression,[p[2]])

def p_expression_types_array_call(p):
    'expression : ID "[" NUMBER "]"'
    p[0]=Node(Expr.ArrayCallExpression,[p[1],p[3]])

def p_expression_types_list(p):
    'expression : "(" expression_list ")"'
    p[0]=Node(Expr.ListExpression,[p[2]])


