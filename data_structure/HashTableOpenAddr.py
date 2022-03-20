class Element:
    """Element in hash table"""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        return
    
    def __str__(self):
        return f'{self.key} : {self.value}'
    
class HashTable:
    """HashTable with open addressing"""
    
    def __init__(self, capacity : int) -> None:
        self._capacity = capacity
        ## empty array
        self._table = [None for _ in range(self._capacity)]
        return
    
    def _hash_function(self, key):
        return hash(key) % self._capacity
    
    def _find_empty_space(self, key):
        """Find empty space in hash table.
        If hash table is full, return None

        Parameters
        ----------
        key : any
            Key value for search space

        Returns
        -------
        int
            Index of empty space in hash table
        """
        
        iter_index = self._hash_function(key)
        for _ in range(self._capacity):
            if self._table[iter_index] is None:
                return iter_index
            
            ## if element with same key is in table,
            ## return index for over-write
            if self._table[iter_index].key == key:
                return iter_index
            
            if iter_index < self._capacity - 1:
                iter_index += 1
            else:
                iter_index = 0
                
        return None
        
    def insert(self, key, value):

        empty_index = self._find_empty_space(key)
        ## if empty space exist, insert element
        if empty_index is not None:
            ele = Element(key, value)
            self._table[empty_index] = ele
        ## else, nothing to do...
        else:
            print(f'Hash table is already full...')
        
        return None

    def _find_element(self, key):
        ...
        
    def delete(self, key):
        ...
    
    def look_up_value(self, key):
        hashed_index = self._hash_function(key)
        
        iter_index = hashed_index
        ## worst case : iterate all elements in table
        for _ in range(self._capacity):
            ## if element is None, no element in table
            if self._table[iter_index] is None:
                return None
            
            ## find key, value pair
            if self._table[iter_index].key == key:
                return self._table[iter_index].value
            
            ## linear probing
            if iter_index < self._capacity - 1:
                iter_index += 1
            else:
                iter_index = 0
    
        return None
    
    def __str__(self):
        
        res_str = ''
        for ele in self._table:
            if ele is not None:
                res_str += f'{str(ele)}\n'
        return res_str[:-1]

if __name__ == '__main__':
    
    ## test _find_empty_space method
    table = HashTable(50)
    print(table._find_empty_space(20))
    
    ## test insert method
    table.insert(20, 20)
    table.insert(30, 30)
    table.insert(40, 40)
    table.insert(20, 30)
    table.insert(70, 70)
    print(table)
    
    ## test insert method
    print(table.look_up_value(70))
    print(table._table)