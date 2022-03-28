class Node:
    """Node class for BinarySearchTree class"""
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.left_child = None
        self.right_child = None
        return

def print_in_order(node : Node) -> None:
    """Print data in tree by in-order traverse"""
    ## base case
    if node == None:
        return
    ## recursive case
    print_in_order(node.left_child)
    print(node.data)
    print_in_order(node.right_child)
    return

class BinarySearchTree:
    """BinarySearchTree class"""
    def __init__(self):
        self.root = None
        return
    
    def print_sorted_tree(self):
        """Print data in BinarySearchTree"""
        print_in_order(self.root)
        return
    
    def insert(self, data):
        """Insert data at BinarySearchTree"""
        if self.root is None:
            self.root = Node(data)
            return
        
        node = Node(data)
        iter_node = self.root
        while iter_node is not None:
            if data < iter_node.data:
                if iter_node.left_child is None:
                    iter_node.left_child = node
                    node.parent = iter_node
                    return
                else:
                    iter_node = iter_node.left_child
            elif data > iter_node.data:
                if iter_node.right_child is None:
                    iter_node.right_child = node
                    node.parent = iter_node
                    return
                else:
                    iter_node = iter_node.right_child
            else:
                return
        return
    
    def search(self, data) -> Node:
        """Find node whose data is same with input data"""
        iter_node = self.root
        while iter_node is not None:
            if iter_node.data == data:
                return iter_node
            elif iter_node.data > data:
                iter_node = iter_node.left_child
            else:
                iter_node = iter_node.right_child
        return
    
    @staticmethod
    def find_min(node) -> Node:
        """Find node whose data is minumum in tree having input node as root"""
        ## base case
        if node.left_child is None:
            return node
        
        ## recursive case        
        return BinarySearchTree.find_min(node.left_child)

    def delete(self, data):
        """Delete leaf node in tree"""
        node_to_delete = self.search(data)
        parent_node = node_to_delete.parent
        
        ## case 1: node to delete is leaf node
        if node_to_delete.left_child is None and\
        node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = None
                return
            
            if parent_node.left_child is node_to_delete:
                parent_node.left_child = None
            else:
                parent_node.right_child = None
        ## case 2: node to delete has one child node
        elif node_to_delete.left_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.right_child
                self.root.parent = None
                return
            if node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.right_child
            else:
                parent_node.right_child = node_to_delete.right_child
            node_to_delete.right_child.parent = parent_node
        elif node_to_delete.right_child is None:
            if node_to_delete is self.root:
                self.root = node_to_delete.left_child
                self.root.parent = None
                return
            if node_to_delete is parent_node.left_child:
                parent_node.left_child = node_to_delete.left_child
            else:
                parent_node.right_child = node_to_delete.left_child
            node_to_delete.left_child.parent = parent_node
        ## case 3: node to delete has both child nodes
        else:
            successor = BinarySearchTree.find_min(node_to_delete.right_child)
            node_to_delete.data = successor.data
            
            ## del successor
            if successor.right_child is None:
                if successor is successor.parent.right_child:
                    successor.parent.right_child = None
                else:
                    successor.parent.left_child = None
            else:
                if successor is successor.parent.right_child:
                    successor.parent.right_child = successor.right_child
                else:
                    successor.parent.left_child = successor.right_child
                successor.right_child.parent = successor.parent
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
    bst.print_sorted_tree()
    print()
    
    ## test insert method
    bst.insert(7)
    bst.insert(11)
    bst.insert(9)
    bst.insert(17)
    bst.insert(8)
    bst.insert(5)
    bst.insert(19)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(14)
    bst.print_sorted_tree()
    print()
    
    ## test search method
    print(bst.search(7).data)
    print(bst.search(19).data)
    print(bst.search(2).data)
    print(bst.search(20))
    print()
    
    ## test find_min method
    bst = BinarySearchTree()

    bst.insert(7)
    bst.insert(11)
    bst.insert(9)
    bst.insert(17)
    bst.insert(8)
    bst.insert(5)
    bst.insert(19)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(14)

    print(bst.find_min(bst.root).data)
    print(bst.find_min(bst.root.right_child).data)
    print()
        
    ## test delete method
    bst.insert(7)
    bst.insert(11)
    bst.insert(9)
    bst.insert(17)
    bst.insert(8)
    bst.insert(5)
    bst.insert(19)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(14)
    
    ## delete leaf nodes
    # bst.delete(2)
    # bst.delete(4)

    # bst.print_sorted_tree()

    ## delete nodes having only one child
    # bst.delete(5)
    # bst.delete(9)
    
    ## delete nodes having both child
    bst.delete(7)
    bst.delete(11)

    bst.print_sorted_tree()    