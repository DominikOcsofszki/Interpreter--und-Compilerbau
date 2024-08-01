from .Nodes import _Node, Node, Literals
from src.ast.sequences_ast import SequenceExpression
from .Expr_Enum import Expr
from icecream import ic
from src.environment import Env
from .environment import Env

def findEnvWithIdWrite(id,env):
    if env.parent.env_name == "ENV_IMPORTS":
            return env
    parent_env = env
    item = parent_env.env_dict.get(id)
    last_parent = parent_env
    while parent_env and not item:
        last_parent = parent_env
        item = parent_env.env_dict.get(id)
        if item:
            return last_parent
        parent_env = parent_env.parent
        er
    return env


def eval(node:Node | Literals,env:Env):
    ic("=============h1==================")
    ic(node)
    type_Expr = node.type_Expr
    if isinstance(node, Node):
        ic("=============h2==================")
        ic(type_Expr)
        self= node.type_Expr.value(*node.children)
        match type_Expr.value:
            case Expr.ReadIdExpression.value: return env[self.id]
            case Expr.WriteIdExpression.value:
                find_env = findEnvWithIdWrite(self.id_string,env)
                if isinstance(self.value, str) or isinstance(self.value, int):
                    find_env[self.id_string] = self.value
                    return self.value
                else:
                    find_env[self.id_string] = eval(self.value,env)
                    return eval(self.value,env)

            case Expr.PlusExpression:
                self = node.type_Expr.value(*node.children)
                return eval(self.e1,env) + eval(self.e1,env)
            case Expr.SequenceExpression.value:
                self = node.type_Expr.value(*node.children)
                last_result = None
                for sequence in self.sequences:
                    ic(sequence)
                    last_result = eval(sequence,env)
                    #TODO Remove / check env since only needed for last/first time
                return last_result, env
            # case node:
            #     ic("=============h2.3==================")
            #     ic(node)
                # eval(node,env)
    elif isinstance(node, Literals):
        # ic("=============h5===============Literals===")
        # ic(node)
        match type_Expr:
            case Expr.NumberExpression:
                return node.leaf
        # Handle Literals-related logic here
        pass
    else:
        raise NotImplementedError("Not Node or Literal!!!")
        ic("Sth Wrong")
        ic(node)
        ic(type(node))
    ic(f"============{node}===========")
    ic("==============================================")
    ic("=============EVAL missed sth==================")
    ic("==============================================")
    ic("==============================================")


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
