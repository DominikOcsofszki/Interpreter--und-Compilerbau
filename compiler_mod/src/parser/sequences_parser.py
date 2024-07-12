

from ..ast import sequences_ast
from ..ast.sequences_ast import *

from .. import gen_helper

from ..Nodes import Node

generator_sequences = sequences_ast if True else None 
genHelperSequences = gen_helper.GeneratorHelper(sequences_ast.used_procedures_and_classes,generator_sequences)


def p_expression_sequence(p):
    'expression : "{" sequence "}" '
    p[0] = Node("SequenceExpression",p[2])

def p_expression_expressions(p):
    '''sequence :   sequence ";" expression 
                |   expression '''
    p[0] = [p[1]] if len(p) == 2 else [*p[1],p[3]]

generator_sequences = genHelperSequences.set_generator_module_and_check(sequences_ast)
