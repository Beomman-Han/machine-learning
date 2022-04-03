## merge function implementation for merge sort

from typing import List


def merge(
    list1 : List[int],
    list2 : List[int]
    ) -> List[int]:
    
    """Merge from two sorted list to sorted list

    Time Complexity
    ---------------
    O(n)
        n : sum of the length of list1 and list2
    
    Parameters
    ----------
    list1 : List[int]
        sorted list 1
    list2 : List[int]
        sorted list 2
    
    Returns
    -------
    List[int]
        merged sorted list
    """
    
    merged = []
    idx1, idx2 = 0, 0
    while idx1 < len(list1) or idx2 < len(list2):
        if idx1 >= len(list1):
            merged += list2[idx2:]
            break
                
        if idx2 >= len(list2):
            merged += list1[idx1:]
            break
        
        if list1[idx1] <= list2[idx2]:
            merged.append(list1[idx1])
            idx1 += 1
        else:
            merged.append(list2[idx2])
            idx2 += 1

    return merged

def merge_sort(
    my_list: List[int]
    ) -> List[int]:
    """Merge sort by divide and conquer method

    Time Complexity
    ---------------
    O(n*lg n)
        n : length of input list
        
    Parameters
    ----------
    my_list : List[int]
        input list

    Returns
    -------
    List[int]
        sorted list
    """
    
    ## base case (conquer for subproblem)
    if len(my_list) == 1:
        return my_list[:]
    
    ## recursive case (divide)
    left = merge_sort(my_list[:len(my_list) // 2])
    right = merge_sort(my_list[len(my_list) // 2:])
    
    ## combine
    return merge(left, right)

if __name__ == '__main__':
    # 테스트
    print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
    print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
    print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))


    # 테스트
    print(merge([1],[]))
    print(merge([],[1]))
    print(merge([2],[1]))
    print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
    print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
    print(merge([4, 7, 8, 9],[1, 3, 6, 10]))