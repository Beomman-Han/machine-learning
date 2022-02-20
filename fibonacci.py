# n번째 피보나치 수를 리턴
def fib(n: int) -> int:
    """fibonacci by recursive method
    
    Parameters
    ----------
    n : nth section of sequence
    
    Returns
    -------
    int
        nth number of fibonacci sequence
    """
    # 코드를 입력하세요.
    if n <= 2:  ## base case
        return 1
    ## recursive case
    return fib(n - 1) + fib(n - 2)

# 테스트: fib(1)부터 fib(10)까지 출력
for i in range(1, 11):
    print(fib(i))