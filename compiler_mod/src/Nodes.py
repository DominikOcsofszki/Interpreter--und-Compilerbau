
from typing import List, Optional, Union
from .Expr_Enum import Expr

class Node:
    def __init__(self, type: Expr, children: Optional[List['Node']] = None, leaf: Optional[Union[str, int]] = None):
    # def __init__(self,type,children,leaf):
        self.type = type
        if children:
            self.children = children
        else:
            self.children = []
        self.leaf = leaf
        self.current_index = 0
        self.root = False

    def __repr__(self) -> str:
        return print_ast(self)
        return str(self.children)

    def __iter__(self) -> 'Node':
        return self

    def __next__(self) -> 'Node':
        if self.current_index < len(self.children):
            child = self.children[self.current_index]
            self.current_index += 1
            return child
        else:
            self.current_index = 0
            raise StopIteration()
    def setRoot(self):
        self.root = True
    def eval(self,env):
        return str(self)
        if self.root: 
            return str(self)

class Literals(Node):
    def __init__(self,type,leaf):
        super().__init__(type,None,leaf)


def print_ast(node: Node, indent: int = 0) -> str:
    result = ""
    # prefix = "|" + (" " * (indent - 1)) + "--"*indent if indent > 0 else ""
    prefix = "|" +   "--"*indent if indent > 0 else ""
    if type(node) == str:
        #TODO: Remove later when fixed all to Nodes
        result += "->"+node
    else:
        result = "\n"
        result += f"{prefix} ( {node.type}"
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
        result += f"{prefix} {node.type}"
        if node.leaf is not None:
            result += f" {node.leaf}\n"
        else:
            # result += "\n"
            for child in node.children:
                result += print_ast0(child, indent + 1)
    return result
    # return result.rstrip()


