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