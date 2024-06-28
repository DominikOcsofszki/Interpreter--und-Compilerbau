
# from ply.yacc import yacc
# from ply.lex import lex

import pack.ast.bool_ast as bool_ast
from pack.lexer.bool_lexer import *
import pack.parser.gen_helper as gen_helper


tokens = []
#DebugMode: Change bool to True for DebugMode, False to run
gen = bool_ast if True else None 
genHelperBool = gen_helper.GeneratorHelper(bool_ast.used_procedures_and_classes,gen)




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
    # print(p[2])
    lowerp2 = p[2].lower()
    match lowerp2:
        case "and"      : p[0] = gen.AndExpression(p[1],p[3]) 
        case "eqcomp"   : p[0] = gen.EqCompExpression(p[1],p[3]) 
        case "="        : p[0] = gen.EqExpression(p[1],p[3]) 
        case ">="       : p[0] = gen.GeExpression(p[1],p[3]) 
        case ">"        : p[0] = gen.GtExpression(p[1],p[3]) 
        case "<="       : p[0] = gen.LeExpression(p[1],p[3]) 
        case "!="       : p[0] = gen.NotEqCompExpression(p[1],p[3]) 
        case "<"        : p[0] = gen.LtExpression(p[1],p[3]) 
        case "or"       : p[0] = gen.OrExpression(p[1],p[3]) 
        case "nand"     : p[0] = gen.NandExpression(p[1],p[3]) 
        # case "not"      : p[0] = gen.NotEqCompExpression(p[1],p[3]) 


    # p[0] = gen.checkAndReturnBinaryClass(p)

def p_expression_unary_operators_not(p):
    '''expression : NOT expression
    '''
    p[0] = gen.NotBoolExpression(p[2])

def p_expression_bool(p):
    ''' expression : BOOL'''
    p[0] = gen.BoolValueExpression(p[1])

gen = genHelperBool.set_generator_module_and_check(bool_ast)
