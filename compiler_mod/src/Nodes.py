
from typing import List, Optional, Union

from .environment import Env
from .Expr_Enum import Expr

class _Node:
    # def __init__(self, type_Expr: Expr, children: Optional[Union[List['Node'],List]] = None, leaf: Optional[Union[str, int]] = None):
    def __init__(self, type_Expr: Expr):
    # def __init__(self,type,children,leaf):
        self.type_Expr = type_Expr
        if type(self.type_Expr) != Expr:
            print(self.type_Expr)
            print("STH WRONG SHOULD BE type_Expr")
            raise TypeError("Only type_Expr are allowed")

            exit()
        # if children:
        #     self.children = children
        # else:
        #     # self.children = []
        #     self.children = []
        # self.leaf = leaf
        # self.current_index = 0
        # self.root = False

    def __iter__(self):
        pass
    def __repr__(self) -> str:
        # return str(self.type_Expr.name)
        # return print_ast(self)
        return "<" +str(self.__class__.__name__) +":"+ str(self.type_Expr) +">"

    # def __iter__(self) -> '_Node':
    #     return self

    def print_tree(self,node):
        str(print_ast(node))
from icecream import ic
class Literals(_Node):
    def __init__(self,type_Expr,leaf):
        super().__init__(type_Expr)
        self.leaf=leaf
    def __iter__(self) -> '_Node':
        return self.leaf 
        yield self.leaf 
    def __next__(self) -> '_Node':
        raise StopIteration()
        return self.leaf
    def eval(self,env:Env):
        Expr_To_Eval = self.type_Expr.value(self.leaf)
        # print(Expr_To_Eval.sequences)
        # self.print_tree(self)
        #TODO can add Node info here!!!
        return Expr_To_Eval.eval(env)
    def getLiteral(self):
        return self.leaf
    def __len__(self):
        return 1




class Node(_Node):
    def __init__(self,type_Expr:Expr,children):
        super().__init__(type_Expr)
        self.children = children
        self.current_index = 0

    def __len__(self):
        return len(self.children)
    def __iter__(self) -> '_Node':
        return self

    def __next__(self) -> 'Node':
        if self.current_index < len(self.children):
            child = self.children[self.current_index]
            self.current_index += 1
            return child
        else:
            self.current_index = 0
            raise StopIteration()
    def getWriteID(self):
        if len(self.children) != 1:
            raise KeyError("Children for getWriteID should be 1")

        return self.children[0]


    def eval(self,env:Env):
        Expr_To_Eval = self.type_Expr.value(*self.children)
        # print(Expr_To_Eval.sequences)
        # self.print_tree(self)
        return Expr_To_Eval.eval(env)
        # return str(self)
        # 
        # if self.root: 
        #     return str(self)



def print_ast(node: Node, indent: int = 0) -> str:
    result = ""
    # prefix = "|" + (" " * (indent - 1)) + "--"*indent if indent > 0 else ""
    prefix = "|" +   "--"*indent if indent > 0 else ""
    if type(node) == str:
        #TODO: Remove later when fixed all to Nodes
        result += "->"+node
    elif type(node) == list:
        #TODO: Remove later when fixed all to Nodes
        result += "->" + str(node)
    else:
        result = "\n"
        result += f"{prefix} ( {node.type_Expr}"
        if node.leaf is not None:
            result += f" {node.leaf} \n"
        else:
            # result += "\n"
            for child in node.children:
                result += print_ast(child, indent + 1) + ")"
    # return result
    return result.rstrip()




def print_ast0(node: Node, indent: int = 0) -> str:
    result = ""
    prefix = "|" + (" " * (indent - 1)) + "--" if indent > 0 else ""
    if type(node) == str:
        #TODO: Remove later when fixed all to Nodes
        result += "->"+node
    else:
        result = "\n"
        result += f"{prefix} {node.type_Expr}"
        if node.leaf is not None:
            result += f" {node.leaf}\n"
        else:
            # result += "\n"
            for child in node.children:
                result += print_ast0(child, indent + 1)
    return result
    # return result.rstrip()


