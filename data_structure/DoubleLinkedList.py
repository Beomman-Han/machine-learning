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
    
    def __getitem__(self, index : int) -> Type['Node']:
        """Get node by index"""
        
        iterator = self.head
        for _ in range(index):
            try:
                iterator = iterator.next
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
    
    def __str__(self) -> str:
        """Special method for printing LinkedList object"""
        
        delimiter = '->'
        
        string = ''
        iterator = self.head
        while iterator is not None:
            string += f'{str(iterator.data)}->'
            iterator = iterator.next
        string += '*'
                        
        return string

