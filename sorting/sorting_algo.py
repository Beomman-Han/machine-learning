from copy import deepcopy
from typing import TypeVar, List

T = TypeVar('T')

class SortAlgo(object):
    """Implement various sorting algorithms
    """
    
    # def __init__(
    #     self,
    #     _input: List[T]
    #     ) -> None:

    #     self._input = _input
        
    #     return
            
    def selection_sort(self, _input: List[T]) -> List[T]:
        """
        Find proper number at each index position.
        
         -------------
        [4, 2, 7, 9, 3] - find number at index 0 (min : 2)
           -----------
        [2, 4, 7, 9, 3] - find number at index 1 (min : 3)
              --------
        [2, 3, 7, 9, 4] - find number at index 2 (min : 4)
        ...
        
        Time Complexity
        ---------------
        O( n^2 )
            n : length of list
        
        Returns
        -------
        List[T]
            sorted list
        """
        
        sorted_list = deepcopy(_input)
        for i in range(len(sorted_list)):
            min_ele = sorted_list[i]
            min_idx = i
            for j in range(i, len(sorted_list)):
                if sorted_list[j] < min_ele:
                    min_ele = sorted_list[j]
                    min_idx = j
            sorted_list[i], sorted_list[min_idx] = min_ele, sorted_list[i]
            
        return sorted_list
    
    def insertion_sort(self, _input) -> List[T]:
    
        sorted_list = deepcopy(_input)
        for i in range(1, len(sorted_list)):
            for j in range(0, i):
                if sorted_list[j] > sorted_list[i]:
                    ## insert
                    min_val = sorted_list[i]
                    for k in range(i, j, -1):
                        sorted_list[k] = sorted_list[k-1]
                    sorted_list[j] = min_val
                    break
        return sorted_list
    
    def merge_sort(self, _input: List[T]) -> List[T]:
        """Divide and conquer method
        
        1) (divide) divide to two small list
        2) (conquer) sort each small list
        3) (**combine) combind each sorted small list
        
        [4, 2, 7, 9, 3]
         -> [4, 2], [7, 9, 3]
            -> [4], [2]
            -> [7], [9, 3]
                -> [9], [3]
                <- [3, 9]
            <- [3, 7, 9]
            <- [2, 4]
         <- [2, 3, 4, 7, 9]
         
         ** [2, 4], [3, 7, 9]
         [2] -> [2, 3] -> [2, 3, 4] -> [2, 3, 4, 7, 9] 
        """
        
        ## base case
        if len(_input) == 1:
            return deepcopy(_input)

        ## recursive case
        left = self.merge_sort(_input[:len(_input) // 2])
        right = self.merge_sort(_input[len(_input) // 2:])
        
        merged = []
        left_idx, right_idx = 0, 0
        while left_idx < len(left) or right_idx < len(right):
            if left_idx >= len(left):
                merged = merged + right[right_idx:]
                break
            
            if right_idx >= len(right):
                merged = merged + left[left_idx:]
                break
                
            if left[left_idx] <= right[right_idx]:
                merged.append(left[left_idx])
                left_idx += 1
            else:
                merged.append(right[right_idx])
                right_idx += 1
        
        return merged
    
if __name__ == '__main__':
    sorter = SortAlgo()
    print(sorter.merge_sort([4, 2, 7, 9, 3]))
    print(sorter.merge_sort([4, 2, 7, 9, 3, 10, 13, 132, 53, 2, 4, 5, 232]))
    print(sorter.insertion_sort([4, 2, 7, 9, 3, 10, 13, 132, 53, 2, 4, 5, 232]))
    
        