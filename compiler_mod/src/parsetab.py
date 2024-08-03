
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionrightASSIGNrightLAMBDArightLOCALnonassocTHENDOnonassocELSEleftORleftANDNANDleft=NEQSEQleft<>LEGEleft+-left*/rightNOTUMINUSAND AS ASSIGN BOOL CHAR DO ELSE EQ EXTEND FLOAT FOR GE ID IF IMPORT IN LAMBDA LAMBDA_START LE LOCAL LOOP NAND NEQS NOT NUMBER OR STRING STRUCT THEN WHILEexpression : "-" expression %prec UMINUSexpression :   expression "+" expression\n                    | expression "-" expression\n                    | expression \'*\' expression\n                    | expression \'/\' expression\n    expression_list :    expression "," expression_list\n                    |       expression\n    expression : NUMBERexpression : "{" sequence "}" expression : LOCAL ID ASSIGN expression IN expression expression : BOOLexpression : IF expression THEN expression\n    expression : IMPORT ID AS IDsequence :   expression \n                |   sequence ";" expression expression : STRUCT "{" sequence_struct "}" expression : FLOATexpression : IF expression THEN expression ELSE expression\n    expression : IMPORT IDexpression :   expression AND expression\n                    | expression EQ expression\n                    | expression \'=\' expression\n                    | expression \'>\' expression\n                    | expression \'<\' expression\n                    | expression GE expression\n                    | expression LE expression\n                    | expression NEQS expression\n                    | expression OR expression\n                    | expression NAND expression\n    expression :     LAMBDA_START LAMBDA expression\n            |           LAMBDA_START expression_list  LAMBDA expression\n    expression : EXTEND ID "{" sequence_struct "}" expression : STRING expression : LOOP expression DO expression\n    dots :    "."\n        |       "." dots\n    expression : CHAR expression : FOR expression ";" expression ";" expression DO expression\n    expression : ID "(" ")"     \n        |           ID "(" expression_list ")"\n    expression : IDexpression : ID dots ID\n    expression : WHILE expression DO expression\n    dot_expression : dots ID\n                    |   ID dots ID\n    expression : dot_expression "(" ")"\n                |   dot_expression "(" expression_list ")"\n\n    expression : "[" expression_list "]"expression : ID "[" NUMBER "]"expression : NOT expression \n    expression : "(" expression_list ")"expression : ID ASSIGN expressionexpression : dots ID ASSIGN expressionseq_assign_expression : dots ID ASSIGN expression \n                        sequence_struct :    seq_assign_expression \n                      |     sequence_struct ";"  seq_assign_expression \n                      '
    
_lr_action_items = {'-':([0,1,2,3,4,6,7,8,11,12,14,15,16,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,41,43,46,47,48,50,51,54,55,58,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80,82,84,85,90,91,92,94,95,96,97,98,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,119,120,122,123,124,125,126,127,128,129,130,],[2,26,2,-8,2,-41,-11,2,-17,2,-33,2,-37,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-1,26,2,2,26,-19,2,26,26,26,26,2,-50,-2,-3,-4,-5,26,26,26,26,26,26,26,26,26,26,-9,2,2,-39,-42,26,2,26,2,2,2,2,-51,2,2,-46,-48,26,26,-40,-49,26,-13,-16,26,26,26,26,26,-47,2,2,2,-32,2,26,26,26,26,2,26,]),'NUMBER':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,45,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,83,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'{':([0,2,4,8,10,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,53,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[4,4,4,4,49,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,93,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'LOCAL':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'BOOL':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'IF':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'IMPORT':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'STRUCT':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'FLOAT':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'LAMBDA_START':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'EXTEND':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'STRING':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'LOOP':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'CHAR':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'FOR':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'ID':([0,2,4,5,8,9,12,13,15,17,18,19,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,44,46,50,59,62,78,79,85,86,89,91,92,94,95,97,98,119,120,122,124,129,],[6,6,6,42,6,48,6,53,6,6,6,57,6,6,6,-35,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,82,6,6,6,-36,6,6,6,107,110,6,6,6,6,6,6,6,6,6,6,6,]),'WHILE':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'[':([0,2,4,6,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[22,22,22,45,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'NOT':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'(':([0,2,4,6,8,12,15,17,18,20,21,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,57,59,78,79,82,85,91,92,94,95,97,98,119,120,122,124,129,],[18,18,18,43,18,18,18,18,18,18,59,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,-44,18,18,18,-45,18,18,18,18,18,18,18,18,18,18,18,18,]),'.':([0,2,4,6,8,12,15,17,18,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,49,50,59,78,79,85,91,92,93,94,95,97,98,109,119,120,122,124,129,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,]),'$end':([1,3,6,7,11,14,16,39,48,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,104,105,106,107,108,112,114,116,117,118,123,125,126,130,],[0,-8,-41,-11,-17,-33,-37,-1,-19,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,-30,-51,-46,-48,-40,-49,-12,-13,-16,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),'+':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[25,-8,-41,-11,-17,-33,-37,-1,25,25,-19,25,25,25,25,-50,-2,-3,-4,-5,25,25,25,25,25,25,25,25,25,25,-9,-39,-42,25,25,-51,-46,-48,25,25,-40,-49,25,-13,-16,25,25,25,25,25,-47,-32,25,25,25,25,25,]),'*':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[27,-8,-41,-11,-17,-33,-37,-1,27,27,-19,27,27,27,27,-50,27,27,-4,-5,27,27,27,27,27,27,27,27,27,27,-9,-39,-42,27,27,-51,-46,-48,27,27,-40,-49,27,-13,-16,27,27,27,27,27,-47,-32,27,27,27,27,27,]),'/':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[28,-8,-41,-11,-17,-33,-37,-1,28,28,-19,28,28,28,28,-50,28,28,-4,-5,28,28,28,28,28,28,28,28,28,28,-9,-39,-42,28,28,-51,-46,-48,28,28,-40,-49,28,-13,-16,28,28,28,28,28,-47,-32,28,28,28,28,28,]),'AND':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[29,-8,-41,-11,-17,-33,-37,-1,29,29,-19,29,29,29,29,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,29,-29,-9,-39,-42,29,29,-51,-46,-48,29,29,-40,-49,29,-13,-16,29,29,29,29,29,-47,-32,29,29,29,29,29,]),'EQ':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[30,-8,-41,-11,-17,-33,-37,-1,30,30,-19,30,30,30,30,-50,-2,-3,-4,-5,30,-21,-22,-23,-24,-25,-26,-27,30,30,-9,-39,-42,30,30,-51,-46,-48,30,30,-40,-49,30,-13,-16,30,30,30,30,30,-47,-32,30,30,30,30,30,]),'=':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[31,-8,-41,-11,-17,-33,-37,-1,31,31,-19,31,31,31,31,-50,-2,-3,-4,-5,31,-21,-22,-23,-24,-25,-26,-27,31,31,-9,-39,-42,31,31,-51,-46,-48,31,31,-40,-49,31,-13,-16,31,31,31,31,31,-47,-32,31,31,31,31,31,]),'>':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[32,-8,-41,-11,-17,-33,-37,-1,32,32,-19,32,32,32,32,-50,-2,-3,-4,-5,32,32,32,-23,-24,-25,-26,32,32,32,-9,-39,-42,32,32,-51,-46,-48,32,32,-40,-49,32,-13,-16,32,32,32,32,32,-47,-32,32,32,32,32,32,]),'<':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[33,-8,-41,-11,-17,-33,-37,-1,33,33,-19,33,33,33,33,-50,-2,-3,-4,-5,33,33,33,-23,-24,-25,-26,33,33,33,-9,-39,-42,33,33,-51,-46,-48,33,33,-40,-49,33,-13,-16,33,33,33,33,33,-47,-32,33,33,33,33,33,]),'GE':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[34,-8,-41,-11,-17,-33,-37,-1,34,34,-19,34,34,34,34,-50,-2,-3,-4,-5,34,34,34,-23,-24,-25,-26,34,34,34,-9,-39,-42,34,34,-51,-46,-48,34,34,-40,-49,34,-13,-16,34,34,34,34,34,-47,-32,34,34,34,34,34,]),'LE':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[35,-8,-41,-11,-17,-33,-37,-1,35,35,-19,35,35,35,35,-50,-2,-3,-4,-5,35,35,35,-23,-24,-25,-26,35,35,35,-9,-39,-42,35,35,-51,-46,-48,35,35,-40,-49,35,-13,-16,35,35,35,35,35,-47,-32,35,35,35,35,35,]),'NEQS':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[36,-8,-41,-11,-17,-33,-37,-1,36,36,-19,36,36,36,36,-50,-2,-3,-4,-5,36,-21,-22,-23,-24,-25,-26,-27,36,36,-9,-39,-42,36,36,-51,-46,-48,36,36,-40,-49,36,-13,-16,36,36,36,36,36,-47,-32,36,36,36,36,36,]),'OR':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[37,-8,-41,-11,-17,-33,-37,-1,37,37,-19,37,37,37,37,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,37,37,-51,-46,-48,37,37,-40,-49,37,-13,-16,37,37,37,37,37,-47,-32,37,37,37,37,37,]),'NAND':([1,3,6,7,11,14,16,39,41,47,48,51,54,55,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,102,103,104,105,106,107,108,112,114,115,116,117,118,123,125,126,127,128,130,],[38,-8,-41,-11,-17,-33,-37,-1,38,38,-19,38,38,38,38,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,38,-29,-9,-39,-42,38,38,-51,-46,-48,38,38,-40,-49,38,-13,-16,38,38,38,38,38,-47,-32,38,38,38,38,38,]),'}':([3,6,7,11,14,16,39,40,41,48,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,87,88,90,96,99,101,102,104,105,106,107,108,112,113,114,116,117,118,121,123,125,126,127,130,],[-8,-41,-11,-17,-33,-37,-1,77,-14,-19,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,108,-55,-30,-51,-46,-48,-15,-40,-49,-12,-13,-16,-31,123,-34,-53,-43,-47,-56,-32,-10,-18,-54,-38,]),';':([3,6,7,11,14,16,39,40,41,48,55,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,87,88,90,96,99,101,102,104,105,106,107,108,112,113,114,115,116,117,118,121,123,125,126,127,130,],[-8,-41,-11,-17,-33,-37,-1,78,-14,-19,95,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,109,-55,-30,-51,-46,-48,-15,-40,-49,-12,-13,-16,-31,109,-34,124,-53,-43,-47,-56,-32,-10,-18,-54,-38,]),'THEN':([3,6,7,11,14,16,39,47,48,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,104,105,106,107,108,112,114,116,117,118,123,125,126,130,],[-8,-41,-11,-17,-33,-37,-1,85,-19,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,-30,-51,-46,-48,-40,-49,-12,-13,-16,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),',':([3,6,7,11,14,16,39,48,51,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,104,105,106,107,108,112,114,116,117,118,123,125,126,130,],[-8,-41,-11,-17,-33,-37,-1,-19,91,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,-30,-51,-46,-48,-40,-49,-12,-13,-16,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),'LAMBDA':([3,6,7,11,12,14,16,39,48,51,52,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,104,105,106,107,108,111,112,114,116,117,118,123,125,126,130,],[-8,-41,-11,-17,50,-33,-37,-1,-19,-7,92,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,-30,-51,-46,-48,-40,-49,-12,-13,-16,-6,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),'DO':([3,6,7,11,14,16,39,48,54,58,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,104,105,106,107,108,112,114,116,117,118,123,125,126,128,130,],[-8,-41,-11,-17,-33,-37,-1,-19,94,98,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,-30,-51,-46,-48,-40,-49,-12,-13,-16,-31,-34,-53,-43,-47,-32,-10,-18,129,-38,]),')':([3,6,7,11,14,16,39,43,48,51,56,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,81,82,84,90,96,99,100,101,104,105,106,107,108,111,112,114,116,117,118,123,125,126,130,],[-8,-41,-11,-17,-33,-37,-1,80,-19,-7,96,99,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,104,-42,-52,-30,-51,-46,118,-48,-40,-49,-12,-13,-16,-6,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),']':([3,6,7,11,14,16,39,48,51,60,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,83,84,90,96,99,101,104,105,106,107,108,111,112,114,116,117,118,123,125,126,130,],[-8,-41,-11,-17,-33,-37,-1,-19,-7,101,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,105,-52,-30,-51,-46,-48,-40,-49,-12,-13,-16,-6,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),'IN':([3,6,7,11,14,16,39,48,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,103,104,105,106,107,108,112,114,116,117,118,123,125,126,130,],[-8,-41,-11,-17,-33,-37,-1,-19,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,-30,-51,-46,-48,119,-40,-49,-12,-13,-16,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),'ELSE':([3,6,7,11,14,16,39,48,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,80,82,84,90,96,99,101,104,105,106,107,108,112,114,116,117,118,123,125,126,130,],[-8,-41,-11,-17,-33,-37,-1,-19,-50,-2,-3,-4,-5,-20,-21,-22,-23,-24,-25,-26,-27,-28,-29,-9,-39,-42,-52,-30,-51,-46,-48,-40,-49,120,-13,-16,-31,-34,-53,-43,-47,-32,-10,-18,-38,]),'ASSIGN':([6,42,57,110,],[46,79,97,122,]),'AS':([48,],[86,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[1,39,41,47,51,54,55,51,58,51,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,51,84,90,51,102,103,106,51,112,114,115,116,117,125,126,127,128,130,]),'dots':([0,2,4,6,8,12,15,17,18,20,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,49,50,59,78,79,85,91,92,93,94,95,97,98,109,119,120,122,124,129,],[19,19,19,44,19,19,19,19,19,19,19,19,62,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,89,19,19,19,19,19,19,19,89,19,19,19,19,89,19,19,19,19,19,]),'dot_expression':([0,2,4,8,12,15,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,43,46,50,59,78,79,85,91,92,94,95,97,98,119,120,122,124,129,],[21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'sequence':([4,],[40,]),'expression_list':([12,18,22,43,59,91,],[52,56,60,81,100,111,]),'sequence_struct':([49,93,],[87,113,]),'seq_assign_expression':([49,93,109,],[88,88,121,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expression","S'",1,None,None,None),
  ('expression -> - expression','expression',2,'p_expr_uminus','literals_parser.py',4),
  ('expression -> expression + expression','expression',3,'p_expression_binary_operators_arith','binop_parser.py',6),
  ('expression -> expression - expression','expression',3,'p_expression_binary_operators_arith','binop_parser.py',7),
  ('expression -> expression * expression','expression',3,'p_expression_binary_operators_arith','binop_parser.py',8),
  ('expression -> expression / expression','expression',3,'p_expression_binary_operators_arith','binop_parser.py',9),
  ('expression_list -> expression , expression_list','expression_list',3,'p_expression_expr_list','lambda_parser.py',7),
  ('expression_list -> expression','expression_list',1,'p_expression_expr_list','lambda_parser.py',8),
  ('expression -> NUMBER','expression',1,'p_expression_num','literals_parser.py',8),
  ('expression -> { sequence }','expression',3,'p_expression_sequence','sequences_parser.py',10),
  ('expression -> LOCAL ID ASSIGN expression IN expression','expression',6,'p_expression_local','local_parser.py',12),
  ('expression -> BOOL','expression',1,'p_expression_bool','literals_parser.py',13),
  ('expression -> IF expression THEN expression','expression',4,'p_expression_if_then','control_parser.py',14),
  ('expression -> IMPORT ID AS ID','expression',4,'p_expression_import_as','import_parser.py',14),
  ('sequence -> expression','sequence',1,'p_expression_seq_expr','sequences_parser.py',15),
  ('sequence -> sequence ; expression','sequence',3,'p_expression_seq_expr','sequences_parser.py',16),
  ('expression -> STRUCT { sequence_struct }','expression',4,'p_expression__new_struct','struct_parser.py',16),
  ('expression -> FLOAT','expression',1,'p_expression_types_float','literals_parser.py',17),
  ('expression -> IF expression THEN expression ELSE expression','expression',6,'p_expression_if_then_else','control_parser.py',18),
  ('expression -> IMPORT ID','expression',2,'p_expression_import','import_parser.py',18),
  ('expression -> expression AND expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',20),
  ('expression -> expression EQ expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',21),
  ('expression -> expression = expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',22),
  ('expression -> expression > expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',23),
  ('expression -> expression < expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',24),
  ('expression -> expression GE expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',25),
  ('expression -> expression LE expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',26),
  ('expression -> expression NEQS expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',27),
  ('expression -> expression OR expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',28),
  ('expression -> expression NAND expression','expression',3,'p_expression_binary_operators_bool','binop_parser.py',29),
  ('expression -> LAMBDA_START LAMBDA expression','expression',3,'p_expression_lambda_args_WORKING','lambda_parser.py',20),
  ('expression -> LAMBDA_START expression_list LAMBDA expression','expression',4,'p_expression_lambda_args_WORKING','lambda_parser.py',21),
  ('expression -> EXTEND ID { sequence_struct }','expression',5,'p_expression_struct_extend','struct_parser.py',20),
  ('expression -> STRING','expression',1,'p_expression_types_string','literals_parser.py',21),
  ('expression -> LOOP expression DO expression','expression',4,'p_expression_loop_do_expr','control_parser.py',24),
  ('dots -> .','dots',1,'p_expression_dots','struct_parser.py',24),
  ('dots -> . dots','dots',2,'p_expression_dots','struct_parser.py',25),
  ('expression -> CHAR','expression',1,'p_expression_types_char','literals_parser.py',25),
  ('expression -> FOR expression ; expression ; expression DO expression','expression',8,'p_expression_for_do_expr','control_parser.py',29),
  ('expression -> ID ( )','expression',3,'p_expression_call_args','lambda_parser.py',29),
  ('expression -> ID ( expression_list )','expression',4,'p_expression_call_args','lambda_parser.py',30),
  ('expression -> ID','expression',1,'p_expression_read_id','literals_parser.py',30),
  ('expression -> ID dots ID','expression',3,'p_expression_dot_outside','struct_parser.py',33),
  ('expression -> WHILE expression DO expression','expression',4,'p_expression_while_do_expr','control_parser.py',34),
  ('dot_expression -> dots ID','dot_expression',2,'p_expression_dot_struct','struct_parser.py',39),
  ('dot_expression -> ID dots ID','dot_expression',3,'p_expression_dot_struct','struct_parser.py',40),
  ('expression -> dot_expression ( )','expression',3,'p_expression_struct_use_parent_WORKING','struct_parser.py',45),
  ('expression -> dot_expression ( expression_list )','expression',4,'p_expression_struct_use_parent_WORKING','struct_parser.py',46),
  ('expression -> [ expression_list ]','expression',3,'p_expression_types_array','binop_parser.py',48),
  ('expression -> ID [ NUMBER ]','expression',4,'p_expression_types_array_call','binop_parser.py',52),
  ('expression -> NOT expression','expression',2,'p_expression_unary_operators_not','struct_parser.py',55),
  ('expression -> ( expression_list )','expression',3,'p_expression_types_list','binop_parser.py',56),
  ('expression -> ID ASSIGN expression','expression',3,'p_expression_write_id','struct_parser.py',60),
  ('expression -> dots ID ASSIGN expression','expression',4,'p_expression_write_id_dots','struct_parser.py',64),
  ('seq_assign_expression -> dots ID ASSIGN expression','seq_assign_expression',4,'p_expression_assign','struct_parser.py',68),
  ('sequence_struct -> seq_assign_expression','sequence_struct',1,'p_expression_expressions_struct','struct_parser.py',75),
  ('sequence_struct -> sequence_struct ; seq_assign_expression','sequence_struct',3,'p_expression_expressions_struct','struct_parser.py',76),
]
