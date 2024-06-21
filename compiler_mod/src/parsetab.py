
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionrightassignrightlambdarightletrecrightlocalnonassocthendononassocelseleftorleftandnandleft=neqseqleft<>legeleft+-left*/rightnotUMINUSBOOL ID NUMBER and as assign char do else eq extend float for ge if import in lambda le letrec local loop nand neqs not or string struct then whileexpression : floatexpression : local ID assign expression in expressionexpression : IDexpression : import ID as IDexpression : letrec ID assign expression lambda expressionexpression : "{" sequence "}" expression :   expression and expression\n                    | expression eq expression\n                    | expression \'=\' expression\n                    | expression \'>\' expression\n                    | expression \'<\' expression\n                    | expression ge expression\n                    | expression le expression\n                    | expression neqs expression\n                    | expression or expression\n                    | expression nand expression\n    expression : string expression : ID assign expressionexpression : import IDexpression : struct "{" sequence "}" expression : "-" expression %prec UMINUSexpression : char expression : if expression then expression\n    expression : ID "." ID sequence :   sequence ";" expression \n                |   expression expression :   expression "+" expression\n                    | expression "-" expression\n                    | expression \'*\' expression\n                    | expression \'/\' expression\n    expression : "[" id_list "]"expression : if expression then expression else expression\n    id_list : expression "," id_list\n        |        expression\n    expression : ID "." ID "(" expression ")"expression : ID "[" NUMBER "]"expression : not expression\n    expression : loop expression do expression\n    expression : extend struct "{" sequence "}" expression : "(" id_list ")"expression : NUMBER expression : BOOLexpression : "(" expression ")"expression : for expression ";" expression ";" expression do expression\n    expression :     lambda expression\n            |           ID lambda expression\n            |           "(" id_list ")" lambda expression\n    expression : while expression do expression\n    expression :  ID "(" ")"expression :  ID "(" id_list ")"'
    
_lr_action_items = {'float':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'local':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'ID':([0,3,5,6,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,39,40,42,48,74,81,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[4,37,43,44,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,76,4,4,4,4,99,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'import':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'letrec':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'{':([0,7,8,10,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,57,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[8,8,8,48,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,92,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'string':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'struct':([0,7,8,11,13,14,15,17,18,19,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[10,10,10,10,10,10,10,10,10,57,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'-':([0,1,2,4,7,8,9,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,43,45,47,48,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,83,84,86,87,88,89,90,91,92,93,94,95,96,97,98,99,100,101,102,103,105,106,108,109,110,111,112,113,114,115,116,117,118,119,120,121,122,123,],[11,34,-1,-3,11,11,-17,11,-22,11,11,11,-41,11,11,-42,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,-19,34,34,11,-21,34,34,34,-37,34,34,34,34,34,34,34,34,34,34,34,34,34,-27,-28,-29,-30,11,34,-24,-49,34,11,-6,11,11,-31,11,-40,-43,11,11,11,11,34,11,-50,-36,-4,34,34,-20,34,11,34,34,34,11,34,11,11,34,-39,11,34,-35,34,34,34,11,34,]),'char':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'if':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'[':([0,4,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[14,41,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'not':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'loop':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'extend':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'(':([0,4,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,76,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[15,40,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,96,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'NUMBER':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,41,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,79,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'BOOL':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'for':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'lambda':([0,2,4,7,8,9,11,12,13,14,15,16,17,18,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,43,45,48,49,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,83,84,86,87,88,89,90,91,92,93,94,96,97,98,99,100,102,103,105,106,109,110,112,113,114,115,116,117,118,119,120,122,123,],[7,-1,42,7,7,-17,7,-22,7,7,7,-41,7,7,-42,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,-19,-45,7,-21,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,7,-18,-24,-49,-46,7,-6,7,7,-31,7,105,-43,7,7,7,7,7,-50,-36,-4,112,-20,-23,7,-38,-48,7,7,7,-47,-39,7,-2,-35,-5,-32,7,-44,]),'while':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'$end':([1,2,4,9,12,16,20,43,45,49,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,97,98,99,102,103,106,109,114,115,117,118,119,120,123,],[0,-1,-3,-17,-22,-41,-42,-19,-45,-21,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,-31,-40,-43,-50,-36,-4,-20,-23,-38,-48,-47,-39,-2,-35,-5,-32,-44,]),'and':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[23,-1,-3,-17,-22,-41,-42,-19,23,23,-21,23,23,23,-37,23,23,23,-7,-8,-9,-10,-11,-12,-13,-14,23,-16,-27,-28,-29,-30,23,-24,-49,23,-6,-31,-40,-43,23,-50,-36,-4,23,23,-20,23,23,23,23,23,23,-39,23,-35,23,23,23,23,]),'eq':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[24,-1,-3,-17,-22,-41,-42,-19,24,24,-21,24,24,24,-37,24,24,24,24,-8,-9,-10,-11,-12,-13,-14,24,24,-27,-28,-29,-30,24,-24,-49,24,-6,-31,-40,-43,24,-50,-36,-4,24,24,-20,24,24,24,24,24,24,-39,24,-35,24,24,24,24,]),'=':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[25,-1,-3,-17,-22,-41,-42,-19,25,25,-21,25,25,25,-37,25,25,25,25,-8,-9,-10,-11,-12,-13,-14,25,25,-27,-28,-29,-30,25,-24,-49,25,-6,-31,-40,-43,25,-50,-36,-4,25,25,-20,25,25,25,25,25,25,-39,25,-35,25,25,25,25,]),'>':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[26,-1,-3,-17,-22,-41,-42,-19,26,26,-21,26,26,26,-37,26,26,26,26,26,26,-10,-11,-12,-13,26,26,26,-27,-28,-29,-30,26,-24,-49,26,-6,-31,-40,-43,26,-50,-36,-4,26,26,-20,26,26,26,26,26,26,-39,26,-35,26,26,26,26,]),'<':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[27,-1,-3,-17,-22,-41,-42,-19,27,27,-21,27,27,27,-37,27,27,27,27,27,27,-10,-11,-12,-13,27,27,27,-27,-28,-29,-30,27,-24,-49,27,-6,-31,-40,-43,27,-50,-36,-4,27,27,-20,27,27,27,27,27,27,-39,27,-35,27,27,27,27,]),'ge':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[28,-1,-3,-17,-22,-41,-42,-19,28,28,-21,28,28,28,-37,28,28,28,28,28,28,-10,-11,-12,-13,28,28,28,-27,-28,-29,-30,28,-24,-49,28,-6,-31,-40,-43,28,-50,-36,-4,28,28,-20,28,28,28,28,28,28,-39,28,-35,28,28,28,28,]),'le':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[29,-1,-3,-17,-22,-41,-42,-19,29,29,-21,29,29,29,-37,29,29,29,29,29,29,-10,-11,-12,-13,29,29,29,-27,-28,-29,-30,29,-24,-49,29,-6,-31,-40,-43,29,-50,-36,-4,29,29,-20,29,29,29,29,29,29,-39,29,-35,29,29,29,29,]),'neqs':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[30,-1,-3,-17,-22,-41,-42,-19,30,30,-21,30,30,30,-37,30,30,30,30,-8,-9,-10,-11,-12,-13,-14,30,30,-27,-28,-29,-30,30,-24,-49,30,-6,-31,-40,-43,30,-50,-36,-4,30,30,-20,30,30,30,30,30,30,-39,30,-35,30,30,30,30,]),'or':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[31,-1,-3,-17,-22,-41,-42,-19,31,31,-21,31,31,31,-37,31,31,31,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,31,-24,-49,31,-6,-31,-40,-43,31,-50,-36,-4,31,31,-20,31,31,31,31,31,31,-39,31,-35,31,31,31,31,]),'nand':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[32,-1,-3,-17,-22,-41,-42,-19,32,32,-21,32,32,32,-37,32,32,32,-7,-8,-9,-10,-11,-12,-13,-14,32,-16,-27,-28,-29,-30,32,-24,-49,32,-6,-31,-40,-43,32,-50,-36,-4,32,32,-20,32,32,32,32,32,32,-39,32,-35,32,32,32,32,]),'+':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[33,-1,-3,-17,-22,-41,-42,-19,33,33,-21,33,33,33,-37,33,33,33,33,33,33,33,33,33,33,33,33,33,-27,-28,-29,-30,33,-24,-49,33,-6,-31,-40,-43,33,-50,-36,-4,33,33,-20,33,33,33,33,33,33,-39,33,-35,33,33,33,33,]),'*':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[35,-1,-3,-17,-22,-41,-42,-19,35,35,-21,35,35,35,-37,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-29,-30,35,-24,-49,35,-6,-31,-40,-43,35,-50,-36,-4,35,35,-20,35,35,35,35,35,35,-39,35,-35,35,35,35,35,]),'/':([1,2,4,9,12,16,20,43,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,100,101,102,103,106,108,109,111,114,115,117,118,119,120,121,123,],[36,-1,-3,-17,-22,-41,-42,-19,36,36,-21,36,36,36,-37,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-29,-30,36,-24,-49,36,-6,-31,-40,-43,36,-50,-36,-4,36,36,-20,36,36,36,36,36,36,-39,36,-35,36,36,36,36,]),'}':([2,4,9,12,16,20,43,45,46,47,49,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,85,87,89,90,97,98,99,101,102,103,106,107,109,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,-19,-45,83,-26,-21,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,102,-31,-40,-43,-50,-36,-4,-25,-20,-23,-38,115,-48,-47,-39,-2,-35,-5,-32,-44,]),';':([2,4,9,12,16,20,43,45,46,47,49,55,58,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,85,87,89,90,97,98,99,101,102,103,106,107,108,109,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,-19,-45,84,-26,-21,-37,93,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,84,-31,-40,-43,-50,-36,-4,-25,-20,-23,-38,84,116,-48,-47,-39,-2,-35,-5,-32,-44,]),'then':([2,4,9,12,16,20,43,45,49,50,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,97,98,99,102,103,106,109,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,-19,-45,-21,86,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,-31,-40,-43,-50,-36,-4,-20,-23,-38,-48,-47,-39,-2,-35,-5,-32,-44,]),',':([2,4,9,12,16,20,43,45,49,52,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,97,98,99,102,103,106,109,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,-19,-45,-21,88,88,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,-31,-40,-43,-50,-36,-4,-20,-23,-38,-48,-47,-39,-2,-35,-5,-32,-44,]),']':([2,4,9,12,16,20,43,45,49,51,52,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,79,80,83,87,89,90,97,98,99,102,103,104,106,109,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,-19,-45,-21,87,-34,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,98,-46,-6,-31,-40,-43,-50,-36,-4,-20,-23,-33,-38,-48,-47,-39,-2,-35,-5,-32,-44,]),')':([2,4,9,12,16,20,40,43,45,49,52,53,54,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,78,80,83,87,89,90,97,98,99,102,103,104,106,109,111,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,77,-19,-45,-21,-34,89,90,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,97,-46,-6,-31,-40,-43,-50,-36,-4,-20,-23,-33,-38,-48,118,-47,-39,-2,-35,-5,-32,-44,]),'do':([2,4,9,12,16,20,43,45,49,55,56,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,97,98,99,102,103,106,109,114,115,117,118,119,120,121,123,],[-1,-3,-17,-22,-41,-42,-19,-45,-21,-37,91,94,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,-31,-40,-43,-50,-36,-4,-20,-23,-38,-48,-47,-39,-2,-35,-5,-32,122,-44,]),'in':([2,4,9,12,16,20,43,45,49,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,95,97,98,99,102,103,106,109,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,-19,-45,-21,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,-31,-40,-43,110,-50,-36,-4,-20,-23,-38,-48,-47,-39,-2,-35,-5,-32,-44,]),'else':([2,4,9,12,16,20,43,45,49,55,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,76,77,80,83,87,89,90,97,98,99,102,103,106,109,114,115,117,118,119,120,123,],[-1,-3,-17,-22,-41,-42,-19,-45,-21,-37,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-27,-28,-29,-30,-18,-24,-49,-46,-6,-31,-40,-43,-50,-36,-4,-20,113,-38,-48,-47,-39,-2,-35,-5,-32,-44,]),'assign':([4,37,44,],[38,74,82,]),'.':([4,],[39,]),'as':([43,],[81,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,7,8,11,13,14,15,17,18,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,38,40,42,48,74,82,84,86,88,91,92,93,94,96,105,110,112,113,116,122,],[1,45,47,49,50,52,54,55,56,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,75,52,80,47,95,100,101,103,52,106,47,108,109,111,114,117,119,120,121,123,]),'sequence':([8,48,92,],[46,85,107,]),'id_list':([14,15,40,88,],[51,53,78,104,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> float','expression',1,'p_expression_types_float','types_parser.py',12),
  ('expression -> local ID assign expression in expression','expression',6,'p_expression_local','local_parser.py',13),
  ('expression -> ID','expression',1,'p_expression_read_id','var_parser.py',13),
  ('expression -> import ID as ID','expression',4,'p_expression_import_as','import_parser.py',14),
  ('expression -> letrec ID assign expression lambda expression','expression',6,'p_expression_letrec','letrec_parser.py',14),
  ('expression -> { sequence }','expression',3,'p_expression_sequence','sequences_parser.py',14),
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
  ('expression -> string','expression',1,'p_expression_types_string','types_parser.py',16),
  ('expression -> ID assign expression','expression',3,'p_expression_write_id','var_parser.py',17),
  ('expression -> import ID','expression',2,'p_expression_import','import_parser.py',18),
  ('expression -> struct { sequence }','expression',4,'p_expression_struct','struct_parser.py',18),
  ('expression -> - expression','expression',2,'p_expr_uminus','top_parser.py',19),
  ('expression -> char','expression',1,'p_expression_types_char','types_parser.py',20),
  ('expression -> if expression then expression','expression',4,'p_expression_if_then','control_parser.py',21),
  ('expression -> ID . ID','expression',3,'p_expression_struct_use','struct_parser.py',22),
  ('sequence -> sequence ; expression','sequence',3,'p_expression_expressions','sequences_parser.py',23),
  ('sequence -> expression','sequence',1,'p_expression_expressions','sequences_parser.py',24),
  ('expression -> expression + expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',24),
  ('expression -> expression - expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',25),
  ('expression -> expression * expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',26),
  ('expression -> expression / expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',27),
  ('expression -> [ id_list ]','expression',3,'p_expression_types_array','types_parser.py',24),
  ('expression -> if expression then expression else expression','expression',6,'p_expression_if_then_else','control_parser.py',25),
  ('id_list -> expression , id_list','id_list',3,'p_expression_expr_ids2','lambda_parser.py',26),
  ('id_list -> expression','id_list',1,'p_expression_expr_ids2','lambda_parser.py',27),
  ('expression -> ID . ID ( expression )','expression',6,'p_expression_struct_use_fn','struct_parser.py',27),
  ('expression -> ID [ NUMBER ]','expression',4,'p_expression_types_array_call','types_parser.py',28),
  ('expression -> not expression','expression',2,'p_expression_unary_operators','bool_parser.py',30),
  ('expression -> loop expression do expression','expression',4,'p_expression_loop_do_expr','control_parser.py',31),
  ('expression -> extend struct { sequence }','expression',5,'p_expression_struct_extend','struct_parser.py',32),
  ('expression -> ( id_list )','expression',3,'p_expression_types_list','types_parser.py',32),
  ('expression -> NUMBER','expression',1,'p_expression_num','arith_parser.py',33),
  ('expression -> BOOL','expression',1,'p_expression_bool','bool_parser.py',35),
  ('expression -> ( expression )','expression',3,'p_expression_paren','arith_parser.py',37),
  ('expression -> for expression ; expression ; expression do expression','expression',8,'p_expression_for_do_expr','control_parser.py',42),
  ('expression -> lambda expression','expression',2,'p_expression_lambda_args','lambda_parser.py',44),
  ('expression -> ID lambda expression','expression',3,'p_expression_lambda_args','lambda_parser.py',45),
  ('expression -> ( id_list ) lambda expression','expression',5,'p_expression_lambda_args','lambda_parser.py',46),
  ('expression -> while expression do expression','expression',4,'p_expression_while_do_expr','control_parser.py',47),
  ('expression -> ID ( )','expression',3,'p_expression_call_no_vars','lambda_parser.py',62),
  ('expression -> ID ( id_list )','expression',4,'p_expression_call_args','lambda_parser.py',66),
]
