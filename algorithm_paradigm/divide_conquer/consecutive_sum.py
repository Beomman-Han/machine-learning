def consecutive_sum(
    start : int,
    end : int
    ) -> int:
    """Calculate the sum of 
    all consecutive number from start to end.
    ** Use divide and conquer method
    
    Time Complexity
    ---------------
    O(lg n)
        n : start ~ end

    Parameters
    ----------
    start : int
        start number
    end : int
        end number

    Returns
    -------
    int
        sum of consecutive numbers
    """
    
    ## base case
    if start == end:
        return start

    ## recursive case
    return consecutive_sum(start, (start+end)//2) + consecutive_sum((start+end)//2+1, end)
    

# 테스트
print(consecutive_sum(1, 10))
print(consecutive_sum(1, 100))
print(consecutive_sum(1, 253))
print(consecutive_sum(1, 388))