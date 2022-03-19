from typing import Type, TypeVar, Protocol

C = TypeVar('C', bound='Comparable')
class Comparable(Protocol):
    """Comparable class containing methods for comparison"""
    
    def __eq__(self: C, other: C) -> bool:
        ...
    def __gt__(self: C, other: C) -> bool:
        ...
    def __lt__(self: C, other: C) -> bool:
        ...
    def __ge__(self: C, other: C) -> bool:
        ...
    def __le__(self: C, other: C) -> bool:
        ...

E = TypeVar('E')

class Node:
    """Node class for double linked list element"""
    
    def __init__(self,
        data : C
        ) -> None:
        
        self.data = data
        self.prev: Type['Node'] = None
        self.next: Type['Node'] = None
        return


class DoubleLinkedList:    
    """Double linked list class"""
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        return
    
    def append(self, data : E) -> None:
        """Append node with data"""
        
        ...
        new_node = Node(data)
        
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        return
        
    def __getitem__(self, index : int) -> Type['Node']:
        """Get node by index"""
        
        if index >= 0:
            iterator = self.head
            for _ in range(index):
                try:
                    iterator = iterator.next
                except AttributeError:
                    raise Exception('IndexError: index out of range')
        else:
            iterator = self.tail
            for _ in range(-1 * index - 1):
                try:
                    iterator = iterator.prev
                except AttributeError:
                    raise Exception('IndexError: index out of range')
        
        return iterator
    
    def find(self, data : E) -> Type['Node']:
        """Find node containing input data"""
        
        iterator = self.head
        while iterator is not None:
            if iterator.data == data:
                return iterator
            iterator = iterator.next
        return iterator
    
    def insert_after(self,
        previous_node : Type['Node'],
        data : E
        ) -> None:
        """Insert node after previous node"""
        
        new_node = Node(data)
        if previous_node is self.tail:
            self.append(data)
        else:
            new_node.prev = previous_node
            new_node.next = previous_node.next
            
            previous_node.next.prev = new_node
            previous_node.next = new_node
            
        return    
    def __str__(self) -> str:
        """Special method for printing LinkedList object"""
        
        delimiter = '<->'
        
        string = ''
        iterator = self.head
        while iterator is not None:
            string += f'{str(iterator.data)}{delimiter}'
            iterator = iterator.next
        string += '*'
                        
        return string

if __name__ == '__main__':
    
    def main():
        
        head_node = Node(2)
        node_1 = Node(3)
        node_2 = Node(5)
        node_3 = Node(7)
        tail_node = Node(11)
        
        head_node.next = node_1
        node_1.prev = head_node
        node_1.next = node_2
        node_2.prev = node_1
        node_2.next = node_3
        node_3.prev = node_2
        node_3.next = tail_node
        tail_node.prev = node_3
        
        my_list = DoubleLinkedList()
        my_list.append(2)
        my_list.append(3)
        my_list.append(5)
        my_list.append(7)
        my_list.append(11)
        
        print(my_list)
        print(my_list[1].data)
        print(my_list[-1].data)
        
        print(my_list)
        my_list.insert_after(my_list[-1], 50)
        print(my_list)
        print(my_list[-1].prev.data)
        print(my_list[-2].next.data)

        return
    
    main()