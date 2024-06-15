
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionrightassignrightlambdaleft,nonassocthennonassocelsedoleftorleftandnandleft=neqseqleft<>legeleft+-left*/right([left)]rightnotUMINUSBOOL ID NUMBER and array as assign char do else eq float for ge if import in lambda le letrec list local loop nand neqs not or string then whileexpression : floatexpression : local ID assign expression in expressionexpression : IDexpression : import ID as IDexpression : ID lambda expressionexpression : "{" sequence "}" expression :   expression and expression\n                    | expression eq expression\n                    | expression \'=\' expression\n                    | expression \'>\' expression\n                    | expression \'<\' expression\n                    | expression ge expression\n                    | expression le expression\n                    | expression neqs expression\n                    | expression or expression\n                    | expression nand expression\n    expression : string expression : letrec ID assign expression in expressionexpression : ID assign expressionexpression : "-" expression %prec UMINUSexpression : import IDsequence :   sequence ";" expression \n                |   expression id_list : expression "," id_list\n        |           expression\n    expression : char expression : if expression then expression\n    expression :   expression "+" expression\n                    | expression "-" expression\n                    | expression \'*\' expression\n                    | expression \'/\' expression\n    expression : "[" id_list "]"expression : if expression then expression else expression\n    expression : ID "[" NUMBER "]"expression : "(" id_list ")" lambda expressionexpression : not expression\n    expression : loop expression do expression\n    expression : "(" id_list ")"expression : NUMBERexpression :  ID "(" id_list ")" expression : BOOLexpression : "(" expression ")"expression : for expression ";" expression ";" expression do expression\n    expression : while expression do expression\n    '
    
_lr_action_items = {'float':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,]),'local':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'ID':([0,3,5,6,8,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,72,74,75,76,78,81,82,83,92,96,97,98,100,105,],[4,34,39,4,42,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,87,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'import':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'{':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,]),'string':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'letrec':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'-':([0,1,2,4,6,7,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,73,74,75,76,77,78,79,80,81,82,83,84,85,86,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,105,106,],[9,31,-1,-3,9,-17,9,-26,9,9,-39,9,9,9,-41,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,-21,31,-20,31,31,31,-36,31,31,31,31,31,31,31,31,31,31,31,31,31,-28,-29,-30,-31,9,31,31,-6,9,9,9,-32,9,-38,-42,9,9,9,31,-34,-40,-4,31,31,31,9,31,31,31,9,9,9,31,9,31,31,31,31,9,31,]),'char':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'if':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'[':([0,4,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[12,37,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'(':([0,4,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[14,38,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'not':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'loop':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'NUMBER':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,37,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,70,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'BOOL':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'for':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'while':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'$end':([1,2,4,7,10,13,17,39,43,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,85,86,87,90,93,95,99,101,102,103,106,],[0,-1,-3,-17,-26,-39,-41,-21,-20,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,-34,-40,-4,-27,-37,-44,-35,-2,-18,-33,-43,]),'and':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[20,-1,-3,-17,-26,-39,-41,-21,20,-20,20,20,20,-36,20,20,20,-7,-8,-9,-10,-11,-12,-13,-14,20,-16,-28,-29,-30,-31,20,20,-6,-32,-38,-42,20,-34,-40,-4,20,20,20,20,20,20,20,20,20,20,20,20,]),'eq':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[21,-1,-3,-17,-26,-39,-41,-21,21,-20,21,21,21,-36,21,21,21,21,-8,-9,-10,-11,-12,-13,-14,21,21,-28,-29,-30,-31,21,21,-6,-32,-38,-42,21,-34,-40,-4,21,21,21,21,21,21,21,21,21,21,21,21,]),'=':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[22,-1,-3,-17,-26,-39,-41,-21,22,-20,22,22,22,-36,22,22,22,22,-8,-9,-10,-11,-12,-13,-14,22,22,-28,-29,-30,-31,22,22,-6,-32,-38,-42,22,-34,-40,-4,22,22,22,22,22,22,22,22,22,22,22,22,]),'>':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[23,-1,-3,-17,-26,-39,-41,-21,23,-20,23,23,23,-36,23,23,23,23,23,23,-10,-11,-12,-13,23,23,23,-28,-29,-30,-31,23,23,-6,-32,-38,-42,23,-34,-40,-4,23,23,23,23,23,23,23,23,23,23,23,23,]),'<':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[24,-1,-3,-17,-26,-39,-41,-21,24,-20,24,24,24,-36,24,24,24,24,24,24,-10,-11,-12,-13,24,24,24,-28,-29,-30,-31,24,24,-6,-32,-38,-42,24,-34,-40,-4,24,24,24,24,24,24,24,24,24,24,24,24,]),'ge':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[25,-1,-3,-17,-26,-39,-41,-21,25,-20,25,25,25,-36,25,25,25,25,25,25,-10,-11,-12,-13,25,25,25,-28,-29,-30,-31,25,25,-6,-32,-38,-42,25,-34,-40,-4,25,25,25,25,25,25,25,25,25,25,25,25,]),'le':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[26,-1,-3,-17,-26,-39,-41,-21,26,-20,26,26,26,-36,26,26,26,26,26,26,-10,-11,-12,-13,26,26,26,-28,-29,-30,-31,26,26,-6,-32,-38,-42,26,-34,-40,-4,26,26,26,26,26,26,26,26,26,26,26,26,]),'neqs':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[27,-1,-3,-17,-26,-39,-41,-21,27,-20,27,27,27,-36,27,27,27,27,-8,-9,-10,-11,-12,-13,-14,27,27,-28,-29,-30,-31,27,27,-6,-32,-38,-42,27,-34,-40,-4,27,27,27,27,27,27,27,27,27,27,27,27,]),'or':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[28,-1,-3,-17,-26,-39,-41,-21,28,-20,28,28,28,-36,28,28,28,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,28,28,-6,-32,-38,-42,28,-34,-40,-4,28,28,28,28,28,28,28,28,28,28,28,28,]),'nand':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[29,-1,-3,-17,-26,-39,-41,-21,29,-20,29,29,29,-36,29,29,29,-7,-8,-9,-10,-11,-12,-13,-14,29,-16,-28,-29,-30,-31,29,29,-6,-32,-38,-42,29,-34,-40,-4,29,29,29,29,29,29,29,29,29,29,29,29,]),'+':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[30,-1,-3,-17,-26,-39,-41,-21,30,-20,30,30,30,-36,30,30,30,30,30,30,30,30,30,30,30,30,30,-28,-29,-30,-31,30,30,-6,-32,-38,-42,30,-34,-40,-4,30,30,30,30,30,30,30,30,30,30,30,30,]),'*':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[32,-1,-3,-17,-26,-39,-41,-21,32,-20,32,32,32,-36,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,-30,-31,32,32,-6,-32,-38,-42,32,-34,-40,-4,32,32,32,32,32,32,32,32,32,32,32,32,]),'/':([1,2,4,7,10,13,17,39,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,88,89,90,93,94,95,99,101,102,103,104,106,],[33,-1,-3,-17,-26,-39,-41,-21,33,-20,33,33,33,-36,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,-30,-31,33,33,-6,-32,-38,-42,33,-34,-40,-4,33,33,33,33,33,33,33,33,33,33,33,33,]),'}':([2,4,7,10,13,17,39,40,41,43,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,85,86,87,88,90,93,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,73,-23,-20,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,-34,-40,-4,-22,-27,-37,-44,-35,-2,-18,-33,-43,]),';':([2,4,7,10,13,17,39,40,41,43,49,51,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,85,86,87,88,90,93,94,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,74,-23,-20,-36,82,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,-34,-40,-4,-22,-27,-37,100,-44,-35,-2,-18,-33,-43,]),'then':([2,4,7,10,13,17,39,43,44,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,85,86,87,90,93,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,-20,76,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,-34,-40,-4,-27,-37,-44,-35,-2,-18,-33,-43,]),',':([2,4,7,10,13,17,39,43,46,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,85,86,87,90,93,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,-20,78,78,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,-34,-40,-4,-27,-37,-44,-35,-2,-18,-33,-43,]),']':([2,4,7,10,13,17,39,43,45,46,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,70,73,77,79,80,85,86,87,90,91,93,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,-20,77,-25,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,85,-6,-32,-38,-42,-34,-40,-4,-27,-24,-37,-44,-35,-2,-18,-33,-43,]),')':([2,4,7,10,13,17,39,43,46,47,48,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,71,73,77,79,80,85,86,87,90,91,93,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,-20,-25,79,80,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,86,-6,-32,-38,-42,-34,-40,-4,-27,-24,-37,-44,-35,-2,-18,-33,-43,]),'do':([2,4,7,10,13,17,39,43,49,50,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,85,86,87,90,93,95,99,101,102,103,104,106,],[-1,-3,-17,-26,-39,-41,-21,-20,-36,81,83,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,-34,-40,-4,-27,-37,-44,-35,-2,-18,-33,105,-43,]),'in':([2,4,7,10,13,17,39,43,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,84,85,86,87,89,90,93,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,-20,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,96,-34,-40,-4,97,-27,-37,-44,-35,-2,-18,-33,-43,]),'else':([2,4,7,10,13,17,39,43,49,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,73,77,79,80,85,86,87,90,93,95,99,101,102,103,106,],[-1,-3,-17,-26,-39,-41,-21,-20,-36,-7,-8,-9,-10,-11,-12,-13,-14,-15,-16,-28,-29,-30,-31,-5,-19,-6,-32,-38,-42,-34,-40,-4,98,-37,-44,-35,-2,-18,-33,-43,]),'lambda':([4,79,],[35,92,]),'assign':([4,34,42,],[36,67,75,]),'as':([39,],[72,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,6,9,11,12,14,15,16,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,35,36,38,67,74,75,76,78,81,82,83,92,96,97,98,100,105,],[1,41,43,44,46,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,68,69,46,84,88,89,90,46,93,94,95,99,101,102,103,104,106,]),'sequence':([6,],[40,]),'id_list':([12,14,38,78,],[45,47,71,91,]),}

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
  ('expression -> ID lambda expression','expression',3,'p_expression_lambda','lambda_parser.py',14),
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
  ('expression -> letrec ID assign expression in expression','expression',6,'p_expression_letrec','local_parser.py',17),
  ('expression -> ID assign expression','expression',3,'p_expression_write_id','var_parser.py',17),
  ('expression -> - expression','expression',2,'p_expr_uminus','top_parser.py',17),
  ('expression -> import ID','expression',2,'p_expression_import','import_parser.py',18),
  ('sequence -> sequence ; expression','sequence',3,'p_expression_expressions','sequences_parser.py',18),
  ('sequence -> expression','sequence',1,'p_expression_expressions','sequences_parser.py',19),
  ('id_list -> expression , id_list','id_list',3,'p_expression_expr_ids2','lambda_parser.py',19),
  ('id_list -> expression','id_list',1,'p_expression_expr_ids2','lambda_parser.py',20),
  ('expression -> char','expression',1,'p_expression_types_char','types_parser.py',20),
  ('expression -> if expression then expression','expression',4,'p_expression_if_then','control_parser.py',21),
  ('expression -> expression + expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',24),
  ('expression -> expression - expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',25),
  ('expression -> expression * expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',26),
  ('expression -> expression / expression','expression',3,'p_expression_binary_operators_arith','arith_parser.py',27),
  ('expression -> [ id_list ]','expression',3,'p_expression_types_array','types_parser.py',24),
  ('expression -> if expression then expression else expression','expression',6,'p_expression_if_then_else','control_parser.py',25),
  ('expression -> ID [ NUMBER ]','expression',4,'p_expression_types_array_call','types_parser.py',28),
  ('expression -> ( id_list ) lambda expression','expression',5,'p_expression_lambda_args','lambda_parser.py',29),
  ('expression -> not expression','expression',2,'p_expression_unary_operators','bool_parser.py',30),
  ('expression -> loop expression do expression','expression',4,'p_expression_loop_do_expr','control_parser.py',31),
  ('expression -> ( id_list )','expression',3,'p_expression_types_list','types_parser.py',32),
  ('expression -> NUMBER','expression',1,'p_expression_num','arith_parser.py',33),
  ('expression -> ID ( id_list )','expression',4,'p_expression_call_args','lambda_parser.py',34),
  ('expression -> BOOL','expression',1,'p_expression_bool','bool_parser.py',35),
  ('expression -> ( expression )','expression',3,'p_expression_paren','arith_parser.py',37),
  ('expression -> for expression ; expression ; expression do expression','expression',8,'p_expression_for_do_expr','control_parser.py',42),
  ('expression -> while expression do expression','expression',4,'p_expression_while_do_expr','control_parser.py',47),
]