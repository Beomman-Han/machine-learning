## Simple hash functions
from typing import Annotated, Type, TypeVar


def hash_function_remainder(
    key : int,
    array_size : int
    ) -> int:
    """Hash function with remainder value

    Parameters
    ----------
    key : int
        Key value for hashing
    array_size : int
        Range of the result of hash function

    Returns
    -------
    int
        Hashing value (remainder from key / array_size)
    """
    
    return key % array_size

from dataclasses import dataclass  ## FIXME find...

@dataclass
class ValueRange:
    min: float
    max: float


def hash_function_multiplication(
    key : int,
    array_size : int,
    a : Annotated[float, ValueRange(0.0, 1.0)]
    ) -> int:
    
    """Hash function with multiplication

    Parameters
    ----------
    key : int
        Key value for hashing
    array_size : int
        Range of the result of hash function
    a : float (0.0 ~ 1.0)
        Specific value for hashing

    Returns
    -------
    int
        Hashing value
    """
    
    return int(array_size * ((a * key) - int(a * key)))


class Node:
    """Node for LinkedList"""
    
    def __init__(self, key, value) -> None:        
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        return


class LinkedList:
    """DoubleLinkedList for hash chaining"""
    
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        return
    
    def find_with_key(self, key) -> Type['Node']:
        
        iterator = self.head
        while iterator is not None:
            if iterator.key == key:
                return iterator
            iterator = iterator.next
        return None
    
    def append(self, key, value) -> None:
        
        new_node = Node(key, value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        return

    def delete(self, node_to_delete : Type['Node']) -> None:
        
        if node_to_delete is self.head:
            self.head = node_to_delete.next
            if node_to_delete is self.tail:
                self.tail = None
            else:
                self.head.prev = None
        elif node_to_delete is self.tail:
            self.tail = node_to_delete.prev
            self.tail.next = None
        else:
            node_to_delete.prev.next = node_to_delete.next
            node_to_delete.next.prev = node_to_delete.prev
        
        return

    def __str__(self) -> str:
        
        res_str = ''
        
        iterator = self.head
        while iterator is not None:
            res_str += f'{iterator.key}: {iterator.value}\n'
            iterator = iterator.next
            
        return res_str


T = TypeVar('T')  ## Immutable types

@dataclass
class KeyRange:
    min: int
    max: int
    
    
class HashTable:
    """HashTable with double LinkedList"""
    
    def __init__(self, capacity : int) -> None:
        self._capacity = capacity
        self._table = [LinkedList() for _ in range(self._capacity)]
        return
    
    # def _hash_function(self, key : T) -> Annotated(int, KeyRange(0, '_capcacity' - 1)):
    def _hash_function(self, key : T) -> int:
        """Hash function with remainder.
        Input key should be immutable type.

        Parameters
        ----------
        key : T
            Immutable type key

        Returns
        -------
        int
            Index number for hash table
        """
        
        return hash(key) % self._capacity
    
    def __str__(self) -> str:

        res_str = ''
        for linked_list in self._table:
            res_str += str(linked_list)
            
        return res_str[:-1]


if __name__ == '__main__':
    ## test hash_function_remainder
    print(hash_function_remainder(40, 200))
    print(hash_function_remainder(120, 200))
    print(hash_function_remainder(788, 200))
    print(hash_function_remainder(2307, 200))
    print()
    
    ## test hash_function_multiplication
    print(hash_function_multiplication(40, 200, 0.61426212))
    print(hash_function_multiplication(120, 200, 0.61426212))
    print(hash_function_multiplication(788, 200, 0.61426212))
    print(hash_function_multiplication(2307, 200, 0.61426212))
    print()
    
    ## test python hash function
    print(hash(12345))
    print(hash(12345))
    print(hash(12346))
    
    print(hash(15.1234))
    print(hash(15.1234))
    print(hash(81.1234))

    # print(hash("파이썬"))
    # print(hash("파이썬"))
    # print(hash("자바"))
    
    print(hash('파이썬'))
    print(hash('파이썬'))
    print(hash('자바'))