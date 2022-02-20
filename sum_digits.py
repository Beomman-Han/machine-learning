# n의 각 자릿수의 합을 리턴
def sum_digits(n: int) -> int:
    """calculate the sum of digits from 'n'
    Time complexity : O(log n) <- not O(n)
    
    recursive case
        sum_digits(22541) -> 22541 % 10 + sum_digits(2254) (22541 // 10)
    base case
        sum_digits(2) -> 2
    
    Parameters
    ----------
    n : int
        input number n

    Returns
    -------
    int
        the sum of digits from inpurt
    """
    
    # 코드를 작성하세요.
    ## base case
    if n // 10 == 0:
        return n
    ## recursive case
    return (n % 10) + sum_digits(n // 10)

# 테스트
print(sum_digits(22541))
print(sum_digits(92130))
print(sum_digits(12634))
print(sum_digits(704))
print(sum_digits(3755))