from .Nodes import _Node, Node, Literals
from src.ast.sequences_ast import SequenceExpression
from .Expr_Enum import Expr
from icecream import ic
from src.environment import Env
from .environment import Env
def eval(node:Node|Literals,env:Env):
    ic("=============h50==================")
    # ic(node)
    ic(node.type_Expr)
    ic(type(node.type_Expr))
    ic(type(node))
    if isinstance(node, Node):
        children = node.children
        ic(children)
        match children:
            case [e1, "+", e2]:
                ic("=============h48==================")
                # e1, env1 = e1.eval(env)
                e1, env1 = eval(e1,env)
                # e2, env2 = e2.eval(env1)
                e2, env1 = eval(e2,env)
                return (e1 + e2)
            case [sequences]:
                ic("=============h47==================")
                ic(sequences)
                # Expr.SequenceExpression
                last_result = None
                for sequence in sequences:
                    ic("=============h49==================")
                    ic(sequence)

                    last_result = eval(sequence,env)
                return last_result, env
            case node:
                ic("=============h46==================")
                ic(node)
                eval(node,env)
    elif isinstance(node, Literals):
        ic("STH WRONG")
        exit()
        match node:
            case "float":
                exit()
        # Handle Literals-related logic here
        pass
    else:
        raise NotImplementedError("Not Node or Literal!!!")
        ic("Sth Wrong")
        ic(node)
        ic(type(node))

# from .Nodes import _Node, Node, Literals
# from src.ast.sequences_ast import SequenceExpression
# from .Expr_Enum import Expr
# from icecream import ic
# from src.environment import Env
# from .environment import Env
# def eval(node:Node|Literals,env:Env):
#     ic("=============h50==================")
#     # ic(node)
#     ic(node.type_Expr)
#     ic(type(node.type_Expr))
#     ic(type(node))
#     if isinstance(node, Node):
#         children = node.children
#         ic(children)
#         match children:
#             case [e1, "+", e2]:
#                 ic("=============h48==================")
#                 # e1, env1 = e1.eval(env)
#                 e1, env1 = eval(e1,env)
#                 # e2, env2 = e2.eval(env1)
#                 e2, env1 = eval(e2,env)
#                 return (e1 + e2)
#             case [sequences]:
#                 ic("=============h47==================")
#                 ic(sequences)
#                 # Expr.SequenceExpression
#                 last_result = None
#                 for sequence in sequences:
#                     ic("=============h49==================")
#                     ic(sequence)
#
#                     last_result = eval(sequence,env)
#                 return last_result, env
#             case node:
#                 ic("=============h46==================")
#                 ic(node)
#                 eval(node,env)
#     elif isinstance(node, Literals):
#         ic("STH WRONG")
#         exit()
#         match node:
#             case "float":
#                 exit()
#         # Handle Literals-related logic here
#         pass
#     else:
#         raise NotImplementedError("Not Node or Literal!!!")
#         ic("Sth Wrong")
#         ic(node)
#         ic(type(node))
#
#
