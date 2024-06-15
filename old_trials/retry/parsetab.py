
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionleftPLUSMINUSleftTIMESDIVIDEleftorleftandnandlefteqnoteqcompeqcompleftltgtlegerightnotDIVIDE LPAREN MINUS NUMBER PLUS RPAREN TIMES and eq eqcomp false ge gt le lt nand not noteqcomp or trueexpression : expression PLUS expressionexpression : expression MINUS expressionexpression : NUMBERexpression : expression TIMES expressionexpression :   expression and expression\n                    | expression eq expression\n                    | expression eqcomp expression\n                    | expression ge expression\n                    | expression gt expression\n                    | expression le expression\n                    | expression lt expression\n                    | expression noteqcomp expression\n                    | expression or expression\n                    | expression nand expression\n    expression : expression DIVIDE expressionexpression : LPAREN expression RPARENexpression :  not expression\n    expression :   false \n                    | true\n\n    '
    
_lr_action_items = {'NUMBER':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'LPAREN':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'not':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'false':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'true':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'$end':([1,2,5,6,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[0,-3,-18,-19,-17,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,]),'PLUS':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[7,-3,-18,-19,7,-17,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,]),'MINUS':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[8,-3,-18,-19,8,-17,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,]),'TIMES':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[9,-3,-18,-19,9,-17,9,9,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,]),'and':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[10,-3,-18,-19,10,-17,10,10,10,-5,-6,-7,-8,-9,-10,-11,-12,10,-14,10,-16,]),'eq':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[11,-3,-18,-19,11,-17,11,11,11,11,-6,-7,-8,-9,-10,-11,-12,11,11,11,-16,]),'eqcomp':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[12,-3,-18,-19,12,-17,12,12,12,12,-6,-7,-8,-9,-10,-11,-12,12,12,12,-16,]),'ge':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[13,-3,-18,-19,13,-17,13,13,13,13,13,13,-8,-9,-10,-11,13,13,13,13,-16,]),'gt':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[14,-3,-18,-19,14,-17,14,14,14,14,14,14,-8,-9,-10,-11,14,14,14,14,-16,]),'le':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[15,-3,-18,-19,15,-17,15,15,15,15,15,15,-8,-9,-10,-11,15,15,15,15,-16,]),'lt':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[16,-3,-18,-19,16,-17,16,16,16,16,16,16,-8,-9,-10,-11,16,16,16,16,-16,]),'noteqcomp':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[17,-3,-18,-19,17,-17,17,17,17,17,-6,-7,-8,-9,-10,-11,-12,17,17,17,-16,]),'or':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[18,-3,-18,-19,18,-17,18,18,18,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,18,-16,]),'nand':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[19,-3,-18,-19,19,-17,19,19,19,-5,-6,-7,-8,-9,-10,-11,-12,19,-14,19,-16,]),'DIVIDE':([1,2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[20,-3,-18,-19,20,-17,20,20,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,]),'RPAREN':([2,5,6,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,],[-3,-18,-19,37,-17,-1,-2,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,7,8,9,10,11,12,13,14,15,16,17,18,19,20,],[1,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression PLUS expression','expression',3,'p_expression_plus','arith_parser.py',18),
  ('expression -> expression MINUS expression','expression',3,'p_expression_minus','arith_parser.py',22),
  ('expression -> NUMBER','expression',1,'p_expression_num','arith_parser.py',26),
  ('expression -> expression TIMES expression','expression',3,'p_expression_times','arith_parser.py',30),
  ('expression -> expression and expression','expression',3,'p_expression_binary_operators','bool_parser.py',31),
  ('expression -> expression eq expression','expression',3,'p_expression_binary_operators','bool_parser.py',32),
  ('expression -> expression eqcomp expression','expression',3,'p_expression_binary_operators','bool_parser.py',33),
  ('expression -> expression ge expression','expression',3,'p_expression_binary_operators','bool_parser.py',34),
  ('expression -> expression gt expression','expression',3,'p_expression_binary_operators','bool_parser.py',35),
  ('expression -> expression le expression','expression',3,'p_expression_binary_operators','bool_parser.py',36),
  ('expression -> expression lt expression','expression',3,'p_expression_binary_operators','bool_parser.py',37),
  ('expression -> expression noteqcomp expression','expression',3,'p_expression_binary_operators','bool_parser.py',38),
  ('expression -> expression or expression','expression',3,'p_expression_binary_operators','bool_parser.py',39),
  ('expression -> expression nand expression','expression',3,'p_expression_binary_operators','bool_parser.py',40),
  ('expression -> expression DIVIDE expression','expression',3,'p_expression_div','arith_parser.py',34),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_paren','arith_parser.py',38),
  ('expression -> not expression','expression',2,'p_expression_unary_operators','bool_parser.py',45),
  ('expression -> false','expression',1,'p_expression_bool','bool_parser.py',50),
  ('expression -> true','expression',1,'p_expression_bool','bool_parser.py',51),
]