import sys
from typing import List, Tuple

from pandas import pivot

def quick_sort_v1(
    input_list: List[int]
    ) -> List[int]:
    """Quick sort version 1 (copy list, inefficient)

    Time Complexity
    ---------------
    ...

    Parameters
    ----------
    input_list : List[int]
        input list

    Returns
    -------
    List[int]
        sorted list
    """

    ## base case (conquer)
    if len(input_list) <= 1:
        return input_list
    
    ## divide
    left, right = divide_by_pivot(input_list)
    
    ## conquer
    left = quick_sort_v1(left)
    right = quick_sort_v1(right)
    
    ## combine
    merged = left + right
    
    return merged

def divide_by_pivot(
    input_list : List[int]
    ) -> Tuple[List[int], List[int]]:
    
    """Align list by last element.
    Elements less than last element locate at left.
    Elements more than last element locate at right.
    
    Parameters
    ----------
    input_list : List[int]
        input list

    Returns
    -------
    Tuple[List[int], List[int]]
        left, right list
    """
    
    ## exception case
    if len(input_list) == 0:
        return [], []
    
    pivot_idx = len(input_list) - 1
    for i in range(len(input_list)):
        if (input_list[i] > input_list[pivot_idx] and i < pivot_idx) or\
            (input_list[i] < input_list[pivot_idx] and i > pivot_idx):
            input_list[pivot_idx], input_list[i] = input_list[i], input_list[pivot_idx]
            pivot_idx = i
        # elif input_list[i] < input_list[pivot_idx] and i > pivot_idx:
        #     input_list[pivot_idx], input_list[i] = input_list[i], input_list[pivot_idx]
        #     pivot_idx = i
    
    return input_list[:pivot_idx], input_list[pivot_idx:]

def swap_elements(
    my_list : List[int],
    index1 : int,
    index2 : int
    ) -> None:
    
    """Swap two element at index1, index2 of list in place.
    
    Parameters
    ----------
    my_list : List[int]
        input list
    index1 : int
        index 1
    index2 : int
        index 2
    """
    
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]
    
    return

def partition(
    my_list : List[int],
    start : int,
    end : int
    ) -> int:
    
    """Partition from start to end of input list for quick sorting.
    Align elements in start~end input list by pivot element.
    
    Time Complexity
    ---------------
    O(n)
        n : the length of input list
        
    Parameters
    ----------
    my_list : List[int]
        input list
    start : int
        start index of input list
    end : int
        end index of input list

    Returns
    -------
    int
        pivot index
    """
    
    big_idx, pivot_idx = start, end
    for i in range(start, end):
        if my_list[i] <= my_list[pivot_idx]:
            swap_elements(my_list, big_idx, i)
            big_idx += 1            
    swap_elements(my_list, big_idx, pivot_idx)
    pivot_idx = big_idx
    big_idx += 1

    return pivot_idx
        
def quicksort(
    my_list : List[int],
    start : int = 0,
    end : int = None
    ) -> None:
    
    """Quick sort implementation (in place sorting)

    Time Complexity
    ---------------
    O(n*lg n) ~ O(n^2)
        n : the length of input list
    
    Parameters
    ----------
    my_list : List[int]
        input list
    start : int
        start index for sorting
    end : int
        end index for sorting
    """
    
    if end == None:
        end = len(my_list) - 1
        
    ## base case
    if start >= end:
        return
    
    ## divide
    pivot_idx = partition(my_list, start, end)
    
    ## conquer and combine (?)
    quicksort(my_list, start, pivot_idx-1)
    quicksort(my_list, pivot_idx+1, end)
    
    return

if __name__ == '__main__':

    # 테스트 1 quicksort
    list1 = [1, 3, 5, 7, 9, 11, 13, 11]
    quicksort(list1, 0, len(list1) - 1)
    print(list1)

    # 테스트 2 quicksort
    list2 = [28, 13, 9, 30, 1, 48, 5, 7, 15]
    quicksort(list2, 0, len(list2) - 1)
    print(list2)

    # 테스트 3 quicksort
    list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
    quicksort(list3, 0, len(list3) - 1)
    print(list3)
    
    # 테스트 3 quicksort
    list3 = [2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]
    quicksort(list3)
    print(list3)

    # # 테스트 1 partition
    # list1 = [4, 3, 6, 2, 7, 1, 5]
    # pivot_index1 = partition(list1, 0, len(list1) - 1)
    # print(list1)
    # print(pivot_index1)

    # # 테스트 2 partition
    # list2 = [6, 1, 2, 6, 3, 5, 4]
    # pivot_index2 = partition(list2, 0, len(list2) - 1)
    # print(list2)
    # print(pivot_index2)

    # input_list = [4,2,1,9,3]
    # print(divide_by_pivot(input_list))
    # print(divide_by_pivot([4,2,1,9,3,6,3]))

    # print(quick_sort_v1([4,2,1,9,3]))
    # print(quick_sort_v1([4,2,1,9,3,6,3]))
