# 파라미터 some_list를 거꾸로 뒤집는 함수
def flip(some_list: list) -> list:
    """make list which of elements are reverse from input list
    Time complexity : O(n^2)

    [5,4,3,2,1] -> flip([4,3,2,1]) + [5]
    [4,3,2,1] -> flip([3,2,1]) + [4]
    ...
    [2,1] -> flip([1]) + [2]
    [1] -> [1]
    
    Parameters
    ----------
    some_list : list
        input list

    Returns
    -------
    list
        reversed list
    """
    
    # 코드를 입력하세요.
    ## base case
    if len(some_list) == 0:  ## O(1)
        return some_list

    ## recursive case
    ## [1][1:] -> []
    return flip(some_list[1:]) + [some_list[0]]  ## O(1) + O(n-1)

def flip_2(some_list: list) -> list:
    """make list which of elements are reverse from input list
    Time complexity : O(n lg n)

    [5,4,3,2,1] -> flip([2,1]) + flip([5,4,3]) ->                -> [1,2,3,4,5]
        [2,1] -> flip([1]) + flip([2]) -> [1,2]
        [5,4,3] -> flip([3]) + flip([5,4])           -> [3,4,5]
            [5,4] -> flip([4]) + flip([5]) -> [4,5]
    
    Parameters
    ----------
    some_list : list
        input list

    Returns
    -------
    list
        reversed list
    """
    
    # 코드를 입력하세요.
    ## base case
    if len(some_list) == 0 or len(some_list) == 1:  ## O(1)
        return some_list

    ## recursive case
    return flip(some_list[len(some_list)//2:]) + flip(some_list[:len(some_list)//2])  ## O(n) + O(n)

# 테스트
# some_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
some_list = [x for x in range(500)]
some_list = flip(some_list)
print(some_list)
some_list = flip_2(some_list)
print(some_list)