
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionleftorleftandnandleft=neqseqleft<>legeleft+-left*/rightnotASSIGN BOOL ID NUMBER and eq ge le nand neqs not orexpression :   expression and expression\n                    | expression eq expression\n                    | expression \'=\' expression\n                    | expression \'>\' expression\n                    | expression \'<\' expression\n                    | expression ge expression\n                    | expression le expression\n                    | expression neqs expression\n                    | expression or expression\n                    | expression nand expression\n    expression :   expression "+" expression\n                    | expression "-" expression\n                    | expression \'*\' expression\n                    | expression \'/\' expression\n    expression : NUMBERexpression : not expression\n    expression : "(" expression ")" expression : BOOL'
    
_lr_action_items = {'NUMBER':([0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'not':([0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'(':([0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'BOOL':([0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'$end':([1,2,5,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[0,-15,-18,-16,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,]),'and':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[6,-15,-18,-16,6,-1,-2,-3,-4,-5,-6,-7,-8,6,-10,-11,-12,-13,-14,-17,]),'eq':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[7,-15,-18,-16,7,7,-2,-3,-4,-5,-6,-7,-8,7,7,-11,-12,-13,-14,-17,]),'=':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[8,-15,-18,-16,8,8,-2,-3,-4,-5,-6,-7,-8,8,8,-11,-12,-13,-14,-17,]),'>':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[9,-15,-18,-16,9,9,9,9,-4,-5,-6,-7,9,9,9,-11,-12,-13,-14,-17,]),'<':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[10,-15,-18,-16,10,10,10,10,-4,-5,-6,-7,10,10,10,-11,-12,-13,-14,-17,]),'ge':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[11,-15,-18,-16,11,11,11,11,-4,-5,-6,-7,11,11,11,-11,-12,-13,-14,-17,]),'le':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[12,-15,-18,-16,12,12,12,12,-4,-5,-6,-7,12,12,12,-11,-12,-13,-14,-17,]),'neqs':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[13,-15,-18,-16,13,13,-2,-3,-4,-5,-6,-7,-8,13,13,-11,-12,-13,-14,-17,]),'or':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[14,-15,-18,-16,14,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,]),'nand':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[15,-15,-18,-16,15,-1,-2,-3,-4,-5,-6,-7,-8,15,-10,-11,-12,-13,-14,-17,]),'+':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[16,-15,-18,-16,16,16,16,16,16,16,16,16,16,16,16,-11,-12,-13,-14,-17,]),'-':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[17,-15,-18,-16,17,17,17,17,17,17,17,17,17,17,17,-11,-12,-13,-14,-17,]),'*':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[18,-15,-18,-16,18,18,18,18,18,18,18,18,18,18,18,18,18,-13,-14,-17,]),'/':([1,2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[19,-15,-18,-16,19,19,19,19,19,19,19,19,19,19,19,19,19,-13,-14,-17,]),')':([2,5,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,],[-15,-18,-16,36,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10,-11,-12,-13,-14,-17,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,3,4,6,7,8,9,10,11,12,13,14,15,16,17,18,19,],[1,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> expression and expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',16),
  ('expression -> expression eq expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',17),
  ('expression -> expression = expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',18),
  ('expression -> expression > expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',19),
  ('expression -> expression < expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',20),
  ('expression -> expression ge expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',21),
  ('expression -> expression le expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',22),
  ('expression -> expression neqs expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',23),
  ('expression -> expression or expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',24),
  ('expression -> expression nand expression','expression',3,'p_expression_binary_operators_bool','bool_parser.py',25),
  ('expression -> expression + expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',22),
  ('expression -> expression - expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',23),
  ('expression -> expression * expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',24),
  ('expression -> expression / expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',25),
  ('expression -> NUMBER','expression',1,'p_expression_num','arith_parser.py',30),
  ('expression -> not expression','expression',2,'p_expression_unary_operators','bool_parser.py',30),
  ('expression -> ( expression )','expression',3,'p_expression_paren','arith_parser.py',34),
  ('expression -> BOOL','expression',1,'p_expression_bool','bool_parser.py',35),
]
