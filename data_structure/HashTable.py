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
        
        ## 'hash(key)' value could change at every running
        return hash(key) % self._capacity
    
    def _get_linked_list_for_key(self, key) -> Type['LinkedList']:
        
        hashed_index = self._hash_function(key)
        return self._table[hashed_index]
    
    def _look_up_node(self, key) -> Type['Node']:
        
        linked_list = self._get_linked_list_for_key(key)
        return linked_list.find_with_key(key)
        
    def look_up_value(self, key : T) -> T:
        """Find value from key: value nodes in hash table

        Parameters
        ----------
        key : T
            Key value

        Returns
        -------
        T
            Value from 'key: value'
        """
        
        node = self._look_up_node(key)        
        return node.value
    
    def insert(self, key, value) -> None:
        """Insert node with key, value at hash table

        Parameters
        ----------
        key : T
            Key value
        value : T
            Value for key
        """
        
        ## check whether replicate node is in linked list
        rep_node = self._look_up_node(key)
        if rep_node is None:
            self._get_linked_list_for_key(key).append(key, value)
        else:
            rep_node.value = value
        return      
    
    def delete_by_key(self, key) -> None:
        
        finding_node = self._look_up_node(key)
        if finding_node is not None:
            linked_list = self._get_linked_list_for_key(key)
            linked_list.delete(finding_node)
        return
        
    
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
    print()
    
    ## test hash table
    test_scores = HashTable(50)  # 시험 점수를 담을 해시 테이블 인스턴스 생성

    # 여러 학생들 이름과 시험 점수 삽입
    test_scores.insert("현승", 85)
    test_scores.insert("영훈", 90)
    test_scores.insert("동욱", 87)
    test_scores.insert("지웅", 99)
    test_scores.insert("신의", 88)
    test_scores.insert("규식", 97)
    test_scores.insert("태호", 90)

    print(test_scores)

    # key인 이름으로 특정 학생 시험 점수 검색
    print(test_scores.look_up_value("현승"))
    print(test_scores.look_up_value("태호"))
    print(test_scores.look_up_value("영훈"))

    # 학생들 시험 점수 수정
    test_scores.insert("현승", 10)
    test_scores.insert("태호", 20)
    test_scores.insert("영훈", 30)

    print(test_scores)
    print()
    
    # 학생들 시험 점수 삭제
    test_scores.delete_by_key("태호")
    test_scores.delete_by_key("지웅")
    test_scores.delete_by_key("신의")
    test_scores.delete_by_key("현승")
    test_scores.delete_by_key("규식")

    print(test_scores)
