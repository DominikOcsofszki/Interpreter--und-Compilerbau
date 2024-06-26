

from pack.ast import sequences_ast_class
from pack.ast.sequences_ast_class import *

import pack.parser.gen_helper as gen_helper


generator_sequences = sequences_ast_class if True else None 
genHelperSequences = gen_helper.GeneratorHelper(sequences_ast_class.used_procedures_and_classes,generator_sequences)


def p_expression_sequence(p):
    'expression : "{" sequence "}"'
    p[0] = generator_sequences.SequenceExpression(p[2])

def p_expression_expressions(p):
    '''sequence :   sequence ";" expression
                |   expression
    '''
    p[0] = [p[1]] if len(p) == 2 else [*p[1],p[3]]
    # p[0] = generator_sequences.ExpressionsExpression(p[1],p[3])

generator_sequences = genHelperSequences.set_generator_module_and_check(sequences_ast_class)
