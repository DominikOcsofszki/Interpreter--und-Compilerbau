









from pack.ast import var_ast_class
from pack.ast.var_ast_class import *

# import pack.lexer.arith_lexer as arith_lexer
import pack.parser.gen_helper as gen_helper


#DebugMode: Change bool to True for DebugMode, False to run
gen_var = var_ast_class if True else None 
# gen_arith = None
genHelperArith = gen_helper.GeneratorHelper(var_ast_class.used_procedures_and_classes,gen_var)


def p_expression_num(p):
    'expression : ID'
    p[0] = gen_var.IdExpression(p[1])

def p_expression_paren(p):
    'expression : expression ASSIGN expression'
    p[0] = gen_var.AssignExpression(p[2])

gen_var = genHelperArith.set_generator_module_and_check(var_ast_class)

# def p_expression_binary_operators_arith(p):
#     '''expression :   expression "+" expression
#                     | expression "-" expression
#                     | expression '*' expression
#                     | expression '/' expression
#     '''
#     p[0] = gen_var.checkAndReturnBinaryClass(p)

