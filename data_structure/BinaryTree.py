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

def swap(
    tree : list,
    index_1 : int,
    index_2 : int
    ) -> None:
    
    """Swap elements at index1 and index2 in tree list

    Parameters
    ----------
    tree : list
        Input tree list
    index_1 : int
        Index1 for swapping
    index_2 : int
        Index2 for swapping
    """
    
    tree[index_1], tree[index_2] = tree[index_2], tree[index_1]    
    
    return

def heapify(
    tree : list,
    index : int,
    tree_size : int
    ) -> None:
    
    """Heapify node at index in tree

    Parameters
    ----------
    tree : list
        Input tree
    index : int
        Index of node to heapify
    tree_size : int
        Input tree size
    """
    
    ## base case
    left_child_index = 2 * index
    right_child_index = 2 * index + 1
    if not (0 < index < tree_size) or not (0 < left_child_index < tree_size):
        return

    ## recursive case
    largest = index
    if tree[largest] < tree[left_child_index]:
        largest = left_child_index
    
    if 0 < right_child_index < tree_size and\
    tree[largest] < tree[right_child_index]:
        largest = right_child_index
    
    if largest != index:
        swap(tree, largest, index)
        heapify(tree, largest, tree_size)

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
    
    ## test heapify function
    tree = [None, 15, 5, 12, 14, 9, 10, 6, 2, 11, 1]  # heapify하려고 하는 완전 이진 트리
    heapify(tree, 2, len(tree))  # 노드 2에 heapify 호출
    print(tree) 