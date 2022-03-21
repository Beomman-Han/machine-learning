from typing import Type, TypeVar


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

def traverse_inorder(node : Type['Node']):
    ## base case
    if node is None:
        return
    
    ## recursive case
    traverse_inorder(node.left_child)
    print(node.data)
    traverse_inorder(node.right_child)

    return

def traverse_preorder(node : Type['Node']):
    ## base case
    if node is None:
        return
    ## recursive case
    print(node.data)
    traverse_preorder(node.left_child)
    traverse_preorder(node.right_child)
    
    return

def traverse_postorder(node : Type['Node']):
    ## base case
    if node is None:
        return
    ## recursive case
    traverse_postorder(node.left_child)
    traverse_postorder(node.right_child)
    print(node.data)

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
    
    ## test traverse functions
    print('## traverse inorder')
    traverse_inorder(root_node)
    print('## traverse preorder')
    traverse_preorder(root_node)
    print('## traverse postorder')
    traverse_postorder(root_node)