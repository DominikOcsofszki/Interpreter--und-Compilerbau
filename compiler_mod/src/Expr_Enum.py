# from ast.arith_ast import ParenExpression
from .ast.binop_ast import AndExpression, BoolValueExpression, DivideExpression, EqCompExpression, EqExpression, GeExpression, GtExpression, LeExpression, LtExpression, MinusExpression, NandExpression, NeqExpression, NotBoolExpression, NotEqCompExpression, NumberExpression, OrExpression,ParenExpression, PlusExpression, TimesExpression
from .ast.control_ast import ForDoExpression, IfThenElseExpression, IfThenExpression, LoopDoExpression, WhileExpression
from .ast.import_ast import ImportAsExpression, ImportExpression
from .ast.lambda_ast import CallExpression, LambdaArgsExpression
from .ast.local_ast import LocalExpression, LocalNewExpression
# from .ast.struct_ast import StructCallNParentWithFunExpression, StructExpression, StructExtendExpression, StructInsideArgsExpression,StructCallFunctionFromOutside, StructVariableFromOutside
from .ast.struct_ast import StructExpression, StructExtendExpression,StructCallFunctionFromOutside, StructVariableFromOutside,WriteIdStructExpression
# from .ast.struct_ast import StructCallFunExpression, StructCallNParentWithFunExpression, StructExpression, StructExtendExpression
from .ast.types_ast import ArrayCallExpression, ArrayExpression, CharExpression, FloatExpression, ListExpression, StringExpression
from .ast.write_read_ast import ReadIdExpression, WriteIdExpression
from .ast.sequences_ast import SequenceExpression

import enum
class Expr(enum.Enum):
    IfThenExpression = IfThenExpression
    IfThenElseExpression = IfThenElseExpression
    WhileExpression = WhileExpression
    ForDoExpression = ForDoExpression
    LoopDoExpression = LoopDoExpression
    FloatExpression = FloatExpression
    CharExpression = CharExpression
    StringExpression = StringExpression
    ArrayExpression = ArrayExpression
    ArrayCallExpression = ArrayCallExpression
    ListExpression = ListExpression
    LocalNewExpression = LocalNewExpression
    LocalExpression = LocalExpression
    WriteIdExpression = WriteIdExpression
    WriteIdStructExpression = WriteIdStructExpression
    ReadIdExpression = ReadIdExpression
    StructExpression = StructExpression
    # StructCallFunExpression = StructCallFunExpression
    StructExtendExpression = StructExtendExpression
    StructCallFunctionFromOutside = StructCallFunctionFromOutside
    StructVariableFromOutside = StructVariableFromOutside
    # StructCallNParentWithFunExpression = StructCallNParentWithFunExpression
    LambdaArgsExpression = LambdaArgsExpression
    CallExpression = CallExpression
    ImportAsExpression = ImportAsExpression
    ImportExpression = ImportExpression
    BoolValueExpression = BoolValueExpression
    LtExpression = LtExpression
    GtExpression = GtExpression
    LeExpression = LeExpression
    GeExpression = GeExpression
    NotEqCompExpression = NotEqCompExpression
    EqCompExpression = EqCompExpression
    AndExpression = AndExpression
    OrExpression = OrExpression
    EqExpression = EqExpression
    NotBoolExpression = NotBoolExpression
    ParenExpression = ParenExpression
    NeqExpression = NeqExpression
    NandExpression = NandExpression
    PlusExpression = PlusExpression
    MinusExpression = MinusExpression
    TimesExpression = TimesExpression
    DivideExpression = DivideExpression
    NumberExpression = NumberExpression
    SequenceExpression = SequenceExpression



# from .ast.sequences_ast import SequenceExpression
#
# import enum
# class Expr(enum.Enum):
#     IfThenExpression = "IfThenExpression"
#     IfThenElseExpression = "IfThenElseExpression"
#     WhileExpression = "WhileExpression"
#     ForDoExpression = "ForDoExpression"
#     LoopDoExpression = "LoopDoExpression"
#     FloatExpression = "FloatExpression"
#     CharExpression = "CharExpression"
#     StringExpression = "StringExpression"
#     ArrayExpression = "ArrayExpression"
#     ArrayCallExpression = "ArrayCallExpression"
#     ListExpression = "ListExpression"
#     LocalNewExpression = "LocalNewExpression"
#     LocalExpression = "LocalExpression"
#     WriteIdExpression = "WriteIdExpression"
#     ReadIdExpression = "ReadIdExpression"
#     ReadParentIdExpression = "ReadParentIdExpression"
#     StructExpression = "StructExpression"
#     StructCallFunExpression = "StructCallFunExpression"
#     StructExtendExpression = "StructExtendExpression"
#     StructCallNParentWithFunExpression = "StructCallNParentWithFunExpression"
#     LambdaArgsExpression = "LambdaArgsExpression"
#     CallExpression = "CallExpression"
#     ImportAsExpression = "ImportAsExpression"
#     ImportExpression = "ImportExpression"
#     BoolValueExpression = "BoolValueExpression"
#     LtExpression = "LtExpression"
#     GtExpression = "GtExpression"
#     LeExpression = "LeExpression"
#     GeExpression = "GeExpression"
#     NotEqCompExpression = "NotEqCompExpression"
#     EqCompExpression = "EqCompExpression"
#     AndExpression = "AndExpression"
#     OrExpression = "OrExpression"
#     EqExpression = "EqExpression"
#     NotBoolExpression = "NotBoolExpression"
#     ParenExpression = "ParenExpression"
#     NeqExpression = "NeqExpression"
#     NandExpression = "NandExpression"
#     PlusExpression = "PlusExpression"
#     MinusExpression = "MinusExpression"
#     TimesExpression = "TimesExpression"
#     DivideExpression = "DivideExpression"
#     NumberExpression = "NumberExpression"
#     SequenceExpression = SequenceExpression
#
