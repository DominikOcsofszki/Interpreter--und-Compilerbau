from pack.ast import call_ast
from pack.ast.call_ast import *

import pack.parser.gen_helper as gen_helper


generator_control = call_ast if True else None 
genHelper = gen_helper.GeneratorHelper(call_ast.used_procedures_and_classes,generator_control)



def p_id_deep(p):
    '''id_deep :   id_deep dot ID 
                |   expression '''

generator_bool = genHelper.set_generator_module_and_check(call_ast)

