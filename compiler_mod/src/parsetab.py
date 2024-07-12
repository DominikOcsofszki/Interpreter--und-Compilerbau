
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'expressionrightASSIGNrightLAMBDArightLOCALnonassocTHENDOnonassocELSEleftORleftANDNANDleft=NEQSEQleft<>LEGEleft+-left*/rightNOTUMINUSAND AS ASSIGN BOOL CHAR DO ELSE EQ EXTEND FLOAT FOR GE ID IF IMPORT IN LAMBDA LAMBDA_START LE LOCAL LOOP NAND NEQS NOT NUMBER OR STRING STRUCT THEN WHILEexpression : "-" expression %prec UMINUSexpression :   expression "+" expression\n                    | expression "-" expression\n                    | expression \'*\' expression\n                    | expression \'/\' expression\n    expression : NUMBERexpression : NOT expression\n    expression : LOCAL ID ASSIGN expression IN expressionexpression_list : expression "," expression_list\n        |        expression\n    expression : IF expression THEN expression\n    expression : IMPORT ID AS IDexpression : "{" sequence "}" sequence_struct :   sequence_struct ";" "." ID ASSIGN expression \n                        |  "." ID ASSIGN expression \n                         expression : BOOLexpression : IF expression THEN expression ELSE expression\n    expression : IMPORT IDexpression :     LAMBDA_START LAMBDA expression\n            |           LAMBDA_START expression_list  LAMBDA expression\n    sequence :   sequence ";" expression \n                |   expression expression :   expression AND expression\n                    | expression EQ expression\n                    | expression \'=\' expression\n                    | expression \'>\' expression\n                    | expression \'<\' expression\n                    | expression GE expression\n                    | expression LE expression\n                    | expression NEQS expression\n                    | expression OR expression\n                    | expression NAND expression\n    expression : FLOATexpression : STRUCT "{" sequence_struct "}" expression : LOOP expression DO expression\n    expression : STRING expression : EXTEND ID "{" sequence_struct "}" expression : ID "(" ")"     \n        |           ID "(" expression_list ")"\n    expression : FOR expression ";" expression ";" expression DO expression\n    expression : CHAR dots :    "."\n        |       "." dots\n    expression : WHILE expression DO expression\n    expression : IDdot_expression : ID dots ID\n                    |   dots ID\n    expression :  dots IDexpression : dot_expression\n                |   dot_expression "(" ")"\n                |   dot_expression "(" expression_list ")"\n\n    expression : ID ASSIGN expressionexpression : dots ID ASSIGN expressionexpression : "[" expression_list "]"expression : ID "[" NUMBER "]"expression : "(" expression_list ")"'
    
_lr_action_items = {'-':([0,1,2,3,4,6,7,9,10,11,12,14,15,17,18,19,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,43,46,47,49,50,51,54,57,58,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,80,82,83,85,86,87,88,89,92,94,95,96,97,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,118,119,121,122,123,124,125,127,128,129,130,131,132,],[2,26,2,-6,2,-45,2,2,-16,2,-33,2,-36,2,2,-41,2,-49,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,-1,-7,2,2,26,-18,26,2,26,26,26,26,-47,2,-2,-3,-4,-5,26,26,26,26,26,26,26,26,26,26,2,-38,26,-46,2,-13,2,26,2,2,2,-56,2,2,2,-50,-54,26,-39,-55,26,-12,26,26,-34,26,26,26,26,-51,2,2,2,-37,2,26,26,26,26,2,2,26,26,]),'NUMBER':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,44,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,81,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,]),'NOT':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,]),'LOCAL':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,]),'IF':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'IMPORT':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,8,]),'{':([0,2,4,7,9,11,13,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,55,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[9,9,9,9,9,9,53,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,93,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'BOOL':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'LAMBDA_START':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'FLOAT':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'STRUCT':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,13,]),'LOOP':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,14,]),'STRING':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,15,]),'EXTEND':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,]),'ID':([0,2,4,5,7,8,9,11,14,16,17,18,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,45,50,60,62,77,83,84,86,88,89,91,92,95,96,97,118,119,120,121,123,129,130,],[6,6,6,41,6,47,6,6,6,55,6,6,6,59,6,-42,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,82,6,6,-43,6,6,105,6,6,6,111,6,6,6,6,6,6,126,6,6,6,6,]),'FOR':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,]),'CHAR':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,]),'WHILE':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,]),'[':([0,2,4,6,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[23,23,23,44,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,23,]),'(':([0,2,4,6,7,9,11,14,17,18,20,22,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,59,60,77,82,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[17,17,17,42,17,17,17,17,17,17,17,60,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,-47,17,17,-46,17,17,17,17,17,17,17,17,17,17,17,17,17,17,]),'.':([0,2,4,6,7,9,11,14,17,18,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,53,60,77,83,86,88,89,92,93,95,96,97,110,118,119,121,123,129,130,],[24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,24,91,24,24,24,24,24,24,24,91,24,24,24,120,24,24,24,24,24,24,]),'$end':([1,3,6,10,12,15,19,22,39,40,47,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,102,103,104,105,108,109,112,115,116,117,122,124,125,132,],[0,-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,-56,-50,-54,-39,-55,-11,-12,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),'+':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[25,-6,-45,-16,-33,-36,-41,-49,-1,-7,25,-18,25,25,25,25,25,-47,-2,-3,-4,-5,25,25,25,25,25,25,25,25,25,25,-38,25,-46,-13,25,-56,-50,-54,25,-39,-55,25,-12,25,25,-34,25,25,25,25,-51,-37,25,25,25,25,25,25,]),'*':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[27,-6,-45,-16,-33,-36,-41,-49,-1,-7,27,-18,27,27,27,27,27,-47,27,27,-4,-5,27,27,27,27,27,27,27,27,27,27,-38,27,-46,-13,27,-56,-50,-54,27,-39,-55,27,-12,27,27,-34,27,27,27,27,-51,-37,27,27,27,27,27,27,]),'/':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[28,-6,-45,-16,-33,-36,-41,-49,-1,-7,28,-18,28,28,28,28,28,-47,28,28,-4,-5,28,28,28,28,28,28,28,28,28,28,-38,28,-46,-13,28,-56,-50,-54,28,-39,-55,28,-12,28,28,-34,28,28,28,28,-51,-37,28,28,28,28,28,28,]),'AND':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[29,-6,-45,-16,-33,-36,-41,-49,-1,-7,29,-18,29,29,29,29,29,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,29,-32,-38,29,-46,-13,29,-56,-50,-54,29,-39,-55,29,-12,29,29,-34,29,29,29,29,-51,-37,29,29,29,29,29,29,]),'EQ':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[30,-6,-45,-16,-33,-36,-41,-49,-1,-7,30,-18,30,30,30,30,30,-47,-2,-3,-4,-5,30,-24,-25,-26,-27,-28,-29,-30,30,30,-38,30,-46,-13,30,-56,-50,-54,30,-39,-55,30,-12,30,30,-34,30,30,30,30,-51,-37,30,30,30,30,30,30,]),'=':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[31,-6,-45,-16,-33,-36,-41,-49,-1,-7,31,-18,31,31,31,31,31,-47,-2,-3,-4,-5,31,-24,-25,-26,-27,-28,-29,-30,31,31,-38,31,-46,-13,31,-56,-50,-54,31,-39,-55,31,-12,31,31,-34,31,31,31,31,-51,-37,31,31,31,31,31,31,]),'>':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[32,-6,-45,-16,-33,-36,-41,-49,-1,-7,32,-18,32,32,32,32,32,-47,-2,-3,-4,-5,32,32,32,-26,-27,-28,-29,32,32,32,-38,32,-46,-13,32,-56,-50,-54,32,-39,-55,32,-12,32,32,-34,32,32,32,32,-51,-37,32,32,32,32,32,32,]),'<':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[33,-6,-45,-16,-33,-36,-41,-49,-1,-7,33,-18,33,33,33,33,33,-47,-2,-3,-4,-5,33,33,33,-26,-27,-28,-29,33,33,33,-38,33,-46,-13,33,-56,-50,-54,33,-39,-55,33,-12,33,33,-34,33,33,33,33,-51,-37,33,33,33,33,33,33,]),'GE':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[34,-6,-45,-16,-33,-36,-41,-49,-1,-7,34,-18,34,34,34,34,34,-47,-2,-3,-4,-5,34,34,34,-26,-27,-28,-29,34,34,34,-38,34,-46,-13,34,-56,-50,-54,34,-39,-55,34,-12,34,34,-34,34,34,34,34,-51,-37,34,34,34,34,34,34,]),'LE':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[35,-6,-45,-16,-33,-36,-41,-49,-1,-7,35,-18,35,35,35,35,35,-47,-2,-3,-4,-5,35,35,35,-26,-27,-28,-29,35,35,35,-38,35,-46,-13,35,-56,-50,-54,35,-39,-55,35,-12,35,35,-34,35,35,35,35,-51,-37,35,35,35,35,35,35,]),'NEQS':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[36,-6,-45,-16,-33,-36,-41,-49,-1,-7,36,-18,36,36,36,36,36,-47,-2,-3,-4,-5,36,-24,-25,-26,-27,-28,-29,-30,36,36,-38,36,-46,-13,36,-56,-50,-54,36,-39,-55,36,-12,36,36,-34,36,36,36,36,-51,-37,36,36,36,36,36,36,]),'OR':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[37,-6,-45,-16,-33,-36,-41,-49,-1,-7,37,-18,37,37,37,37,37,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,37,-46,-13,37,-56,-50,-54,37,-39,-55,37,-12,37,37,-34,37,37,37,37,-51,-37,37,37,37,37,37,37,]),'NAND':([1,3,6,10,12,15,19,22,39,40,46,47,49,51,54,57,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,106,108,109,112,114,115,116,117,122,124,125,127,128,131,132,],[38,-6,-45,-16,-33,-36,-41,-49,-1,-7,38,-18,38,38,38,38,38,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,38,-32,-38,38,-46,-13,38,-56,-50,-54,38,-39,-55,38,-12,38,38,-34,38,38,38,38,-51,-37,38,38,38,38,38,38,]),'THEN':([3,6,10,12,15,19,22,39,40,46,47,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,102,103,104,105,108,109,112,115,116,117,122,124,125,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,83,-18,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,-56,-50,-54,-39,-55,-11,-12,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),'}':([3,6,10,12,15,19,22,39,40,47,48,49,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,90,94,98,100,102,103,104,105,106,108,109,112,113,115,116,117,122,124,125,127,131,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,85,-22,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,109,-56,-50,-54,-39,-55,-11,-12,-21,-20,-34,-35,122,-44,-53,-51,-37,-8,-17,-15,-14,-40,]),';':([3,6,10,12,15,19,22,39,40,47,48,49,57,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,90,94,98,100,102,103,104,105,106,108,109,112,113,114,115,116,117,122,124,125,127,131,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,86,-22,95,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,110,-56,-50,-54,-39,-55,-11,-12,-21,-20,-34,-35,110,123,-44,-53,-51,-37,-8,-17,-15,-14,-40,]),',':([3,6,10,12,15,19,22,39,40,47,51,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,102,103,104,105,108,109,112,115,116,117,122,124,125,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,88,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,-56,-50,-54,-39,-55,-11,-12,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),'LAMBDA':([3,6,10,11,12,15,19,22,39,40,47,51,52,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,102,103,104,105,107,108,109,112,115,116,117,122,124,125,132,],[-6,-45,-16,50,-33,-36,-41,-49,-1,-7,-18,-10,89,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,-56,-50,-54,-39,-55,-11,-12,-9,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),'DO':([3,6,10,12,15,19,22,39,40,47,54,58,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,102,103,104,105,108,109,112,115,116,117,122,124,125,128,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,92,96,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,-56,-50,-54,-39,-55,-11,-12,-20,-34,-35,-44,-53,-51,-37,-8,-17,130,-40,]),')':([3,6,10,12,15,19,22,39,40,42,47,51,56,59,60,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,79,80,82,85,87,94,98,99,100,102,103,104,105,107,108,109,112,115,116,117,122,124,125,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,78,-18,-10,94,-47,98,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,102,-52,-46,-13,-19,-56,-50,117,-54,-39,-55,-11,-12,-9,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),']':([3,6,10,12,15,19,22,39,40,47,51,59,61,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,81,82,85,87,94,98,100,102,103,104,105,107,108,109,112,115,116,117,122,124,125,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,-10,-47,100,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,103,-46,-13,-19,-56,-50,-54,-39,-55,-11,-12,-9,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),'IN':([3,6,10,12,15,19,22,39,40,47,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,101,102,103,104,105,108,109,112,115,116,117,122,124,125,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,-56,-50,-54,118,-39,-55,-11,-12,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),'ELSE':([3,6,10,12,15,19,22,39,40,47,59,63,64,65,66,67,68,69,70,71,72,73,74,75,76,78,80,82,85,87,94,98,100,102,103,104,105,108,109,112,115,116,117,122,124,125,132,],[-6,-45,-16,-33,-36,-41,-49,-1,-7,-18,-47,-2,-3,-4,-5,-23,-24,-25,-26,-27,-28,-29,-30,-31,-32,-38,-52,-46,-13,-19,-56,-50,-54,-39,-55,119,-12,-20,-34,-35,-44,-53,-51,-37,-8,-17,-40,]),'ASSIGN':([6,41,59,111,126,],[43,77,97,121,129,]),'AS':([47,],[84,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expression':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[1,39,40,46,49,51,54,51,57,58,51,63,64,65,66,67,68,69,70,71,72,73,74,75,76,51,80,87,51,101,104,106,51,108,112,114,115,116,124,125,127,128,131,132,]),'dots':([0,2,4,6,7,9,11,14,17,18,20,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[21,21,21,45,21,21,21,21,21,21,21,21,62,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,]),'dot_expression':([0,2,4,7,9,11,14,17,18,20,23,25,26,27,28,29,30,31,32,33,34,35,36,37,38,42,43,50,60,77,83,86,88,89,92,95,96,97,118,119,121,123,129,130,],[22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,22,]),'sequence':([9,],[48,]),'expression_list':([11,17,23,42,60,88,],[52,56,61,79,99,107,]),'sequence_struct':([53,93,],[90,113,]),}

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
  ('expression -> NUMBER','expression',1,'p_expression_num','literals_parser.py',8),
  ('expression -> NOT expression','expression',2,'p_expression_unary_operators_not','literals_parser.py',12),
  ('expression -> LOCAL ID ASSIGN expression IN expression','expression',6,'p_expression_local','local_parser.py',12),
  ('expression_list -> expression , expression_list','expression_list',3,'p_expression_expr_list','lambda_parser.py',13),
  ('expression_list -> expression','expression_list',1,'p_expression_expr_list','lambda_parser.py',14),
  ('expression -> IF expression THEN expression','expression',4,'p_expression_if_then','control_parser.py',14),
  ('expression -> IMPORT ID AS ID','expression',4,'p_expression_import_as','import_parser.py',14),
  ('expression -> { sequence }','expression',3,'p_expression_sequence','sequences_parser.py',15),
  ('sequence_struct -> sequence_struct ; . ID ASSIGN expression','sequence_struct',6,'p_expression_expressions_struct','struct_parser.py',15),
  ('sequence_struct -> . ID ASSIGN expression','sequence_struct',4,'p_expression_expressions_struct','struct_parser.py',16),
  ('expression -> BOOL','expression',1,'p_expression_bool','literals_parser.py',17),
  ('expression -> IF expression THEN expression ELSE expression','expression',6,'p_expression_if_then_else','control_parser.py',18),
  ('expression -> IMPORT ID','expression',2,'p_expression_import','import_parser.py',18),
  ('expression -> LAMBDA_START LAMBDA expression','expression',3,'p_expression_lambda_args_WORKING','lambda_parser.py',19),
  ('expression -> LAMBDA_START expression_list LAMBDA expression','expression',4,'p_expression_lambda_args_WORKING','lambda_parser.py',20),
  ('sequence -> sequence ; expression','sequence',3,'p_expression_expressions','sequences_parser.py',19),
  ('sequence -> expression','sequence',1,'p_expression_expressions','sequences_parser.py',20),
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
  ('expression -> FLOAT','expression',1,'p_expression_types_float','literals_parser.py',21),
  ('expression -> STRUCT { sequence_struct }','expression',4,'p_expression__new_struct','struct_parser.py',22),
  ('expression -> LOOP expression DO expression','expression',4,'p_expression_loop_do_expr','control_parser.py',24),
  ('expression -> STRING','expression',1,'p_expression_types_string','literals_parser.py',25),
  ('expression -> EXTEND ID { sequence_struct }','expression',5,'p_expression_struct_extend','struct_parser.py',26),
  ('expression -> ID ( )','expression',3,'p_expression_call_args','lambda_parser.py',28),
  ('expression -> ID ( expression_list )','expression',4,'p_expression_call_args','lambda_parser.py',29),
  ('expression -> FOR expression ; expression ; expression DO expression','expression',8,'p_expression_for_do_expr','control_parser.py',29),
  ('expression -> CHAR','expression',1,'p_expression_types_char','literals_parser.py',29),
  ('dots -> .','dots',1,'p_expression_dots','struct_parser.py',30),
  ('dots -> . dots','dots',2,'p_expression_dots','struct_parser.py',31),
  ('expression -> WHILE expression DO expression','expression',4,'p_expression_while_do_expr','control_parser.py',34),
  ('expression -> ID','expression',1,'p_expression_read_id','literals_parser.py',34),
  ('dot_expression -> ID dots ID','dot_expression',3,'p_expression_dot_struct','struct_parser.py',36),
  ('dot_expression -> dots ID','dot_expression',2,'p_expression_dot_struct','struct_parser.py',37),
  ('expression -> dots ID','expression',2,'p_expression_read_parent_id','literals_parser.py',38),
  ('expression -> dot_expression','expression',1,'p_expression_struct_use_parent_WORKING','struct_parser.py',42),
  ('expression -> dot_expression ( )','expression',3,'p_expression_struct_use_parent_WORKING','struct_parser.py',43),
  ('expression -> dot_expression ( expression_list )','expression',4,'p_expression_struct_use_parent_WORKING','struct_parser.py',44),
  ('expression -> ID ASSIGN expression','expression',3,'p_expression_write_id','literals_parser.py',43),
  ('expression -> dots ID ASSIGN expression','expression',4,'p_expression_write_id_dots','literals_parser.py',47),
  ('expression -> [ expression_list ]','expression',3,'p_expression_types_array','binop_parser.py',48),
  ('expression -> ID [ NUMBER ]','expression',4,'p_expression_types_array_call','binop_parser.py',52),
  ('expression -> ( expression_list )','expression',3,'p_expression_types_list','binop_parser.py',56),
]
