def binary_search(element, some_list):
    # 코드를 작성하세요.
    element_idx = None
    upper = len(some_list) - 1
    lower = 0
    while True:
        index = ( upper + lower ) // 2
        if some_list[index] == element:
            element_idx = index
            break
        if upper <= lower:  ## break condition (** consider carefully!)
            break

        if some_list[index] > element:
            upper = index - 1
        else:
            lower = index + 1

    return element_idx

# print(binary_search(2, [2, 3, 5, 7, 11]))
# print(binary_search(0, [2, 3, 5, 7, 11]))
# print(binary_search(5, [2, 3, 5, 7, 11]))
# print(binary_search(3, [2, 3, 5, 7, 11]))
# print(binary_search(11, [2, 3, 5, 7, 11]))

from typing import List, TypeVar

T = TypeVar('T')

## recursive method
def binary_search(element: T, some_list: List[T], start_index: int=0, end_index: int=None) -> int:
    """binary search algorithm with recursive way
    Time complexity : O(lg n)
    
        > base case
        1) some_list[middle_index] == element
        2) start_index >= end_index and element not found
        > recursive case
         v       v      v v                  v v
        [1,2,3,4,5] -> [1,2,3,4,5] or [1,2,3,4,5]

    Parameters
    ----------
    element : T
        element for searching
    some_list : List[T]
        list containing elements
    start_index : int, optional
        start index for searching, by default 0
    end_index : int, optional
        end index for searcing, by default None

    Returns
    -------
    int
        index of element for searching, if element is not in list, return None
    """    
    
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    ## base case
    middle_index = ( start_index + end_index ) // 2
    if some_list[middle_index] == element:
        return middle_index
    if start_index >= end_index:
        return None

    ## recursive case
    if some_list[middle_index] > element:
        return binary_search(element, some_list, start_index, middle_index-1)
    else:
        return binary_search(element, some_list, middle_index+1, end_index)

## recursive method
def binary_search_2(element: T, some_list: List[T], start_index: int=0, end_index: int=None) -> int:
    """binary search algorithm with recursive way (2)
    Time complexity : O(lg n)
    
        > base case
        1) some_list[middle_index] == element
        2) len(some_list) == 1 or len(some_list) == 0 and element not found
        > recursive case (if return None -> None)
         v       v      v v      v v
        [1,2,3,4,5] -> [1,2] or [4,5]

    Caution: (tricky cases)
        list[0:0]
        list[0:-1]
        list[2:2]
        ...

    Parameters
    ----------
    element : T
        element for searching
    some_list : List[T]
        list containing elements
    start_index : int, optional
        start index for searching, by default 0
    end_index : int, optional
        end index for searcing, by default None

    Returns
    -------
    int
        index of element for searching, if element is not in list, return None
    """    

    ## base case : []
    if len(some_list) == 0:
        return None
    
    # end_index가 따로 주어지지 않은 경우에는 리스트의 마지막 인덱스
    if end_index == None:
        end_index = len(some_list) - 1

    # 코드를 작성하세요.
    ## base case
    middle_index = ( start_index + end_index ) // 2
    if some_list[middle_index] == element:
        return middle_index
    if len(some_list) == 1:
        return None

    ## recursive case
    if some_list[middle_index] > element:
        try:
            return start_index + binary_search_2(element, some_list[:middle_index])
        except TypeError:
            return None
    else:
        try:
            return middle_index + 1 + binary_search_2(element, some_list[middle_index+1:])
        except TypeError:
            return None


if __name__ == '__main__':

    print(binary_search_2(2, [2, 3, 5, 7, 11]))
    print(binary_search_2(0, [2, 3, 5, 7, 11]))
    print(binary_search_2(5, [2, 3, 5, 7, 11]))
    print(binary_search_2(3, [2, 3, 5, 7, 11]))
    print(binary_search_2(11, [2, 3, 5, 7, 11]))