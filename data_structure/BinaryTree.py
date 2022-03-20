from typing import TypeVar


C = TypeVar('C')  ## Comparable

class Node:
    """Node for binary tree data structure"""
    
    def __init__(self, data : C) -> None:
        """data and two child node references"""
        self.data = data
        self.left_child = None
        self.right_child = None
        return
    
    
class BinaryTree:
    
    def __init__(self, value : C) -> None:
        self.root = Node(value)
        return
    
if __name__ == '__main__':
    
    ## init node instance
    root_node = Node(2)
    node_B = Node(3)
    node_C = Node(5)
    node_D = Node(7)
    node_E = Node(11)
    
    ## connect nodes to binary tree
    root_node.left_child = node_B
    root_node.right_child = node_C
    node_B.left_child = node_D
    node_B.right_child = node_E
    
    ## test binary tree
    test_node_1 = root_node.left_child
    print(test_node_1.data)
    