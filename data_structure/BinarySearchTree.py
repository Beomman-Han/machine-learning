class Node:
    """Node class for BinarySearchTree class"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
        return

class BinarySearchTree:
    """BinarySearchTree class"""
    def __init__(self):
        self.root = None
        return

    def print_sorted_tree(self, node):
        """Print data in tree by in-order traverse"""
        ## base case
        if node == None:
            return
        
        ## recursive case
        self.print_sorted_tree(node.left_child)
        print(node.data)
        self.print_sorted_tree(node.right_child)
        return
        

if __name__ == '__main__':
    
    ## make node instances and connect them
    node_0 = Node(5)
    node_1 = Node(3)
    node_2 = Node(7)
    
    node_0.left_child = node_1
    node_1.parent = node_0
    
    node_0.right_child = node_2
    node_2.parent = node_0
    
    ## make BinarySearchTree instance
    bst = BinarySearchTree()
    bst.root = node_0
    
    bst.print_sorted_tree(bst.root)
    