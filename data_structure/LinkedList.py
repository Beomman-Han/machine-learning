from os import link
from typing import Iterator, Type, TypeVar

E = TypeVar('E')

class Node:
    """Node class for LinkedList element"""
    
    ## memory efficiency and restrict attributes
    __slots__ = ('_data', '_next')
    
    def __init__(self,
        data : E
        ) -> None:
        
        self.data = data
        self.next: Type['Node'] = None
        
        return

    ## data getter/setter (property)
    @property
    def data(self) -> E:
        return self._data
    
    @data.setter
    def data(self, data : E) -> None:
        self._data = data
        return
    
    ## next getter/setter (property)
    @property
    def next(self) -> Type['Node']:
        return self._next
    
    @next.setter
    def next(self, node : Type['Node']) -> None:
        self._next = node
        return
    
    def __str__(self) -> str:
        return str(self.data)

class LinkedList:
    """LinkedList class containing Node objects"""
    
    def __init__(self) -> None:
        
        self.head = None
        self.tail = None

        return
    
    def append(self, data : E) -> None:
        """Append method for adding element at linked list"""
        
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:  
            self.tail.next = new_node
            self.tail = new_node

        return

    def insert_after(self,
        prev_node : Type['Node'],
        data : E
        ) -> None:
        
        """Insert node with 'data' at next of 'prev_node'

        Parameters
        ----------
        prev_node : Type['Node']
            Previous node of insert node
        data : E
            Data for insert
        """
        
        new_node = Node(data)
        
        if prev_node is self.tail:
            self.append(new_node)
        else:
            next_node = prev_node.next
            prev_node.next = new_node
            new_node.next = next_node
            
        return
    
    def delete_after(self, prev_node : Type['Node']) -> E:
        """Delete node after 'prev_node'"""
        
        data = prev_node.next.data
        
        if prev_node.next is self.tail:
            prev_node.next = None
            self.tail = prev_node
        else:
            prev_node.next = prev_node.next.next

        return data
    
    def prepend(self, data : E) -> None:
        """Add node contain data at the first of LinkedList"""
        
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node

        return
    
    def pop_left(self) -> E:
        """Delete the first of LinkedList and return data of deleted node"""
        
        data = self.head.data
        if self.head is self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next

        return data
    
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
    
if __name__ == '__main__':
    
    def main():
        
        ## init nodes
        head_node = Node(2)
        node_1 = Node(3)
        node_2 = Node(5)
        node_3 = Node(7)
        tail_node = Node(11)
        
        ## connect nodes
        head_node.next = node_1
        node_1.next = node_2
        node_2.next = node_3
        node_3.next = tail_node
        
        ## print nodes
        iterator = head_node
        while iterator != None:
            print(iterator.data)
            iterator = iterator.next
        
        linked_list = LinkedList()
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(5)
        linked_list.append(7)
        
        iterator = linked_list.head
        while iterator is not None:
            print(iterator.data)
            iterator = iterator.next
        
        ## test __str__ method
        print(linked_list)
        
        ## test __getitem__ method
        linked_list[0].data = 13
        print(linked_list)
        
        ## test insert after method
        linked_list.insert_after(linked_list[3], 30)
        print(linked_list)
        
        ## test prepend method
        linked_list = LinkedList()

        # 여러 데이터를 링크드 리스트 앞에 추가
        linked_list.prepend(11)
        linked_list.prepend(7)
        linked_list.prepend(5)
        linked_list.prepend(3)
        linked_list.prepend(2)

        print(linked_list)  # 링크드 리스트 출력

        # head, tail 노드가 제대로 설정됐는지 확인
        print(linked_list.head.data)
        print(linked_list.tail.data)
        
        print(linked_list.delete_after(linked_list[2]))
        print(linked_list)
        
        return
    
    main()