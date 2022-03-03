from typing import Dict


def fib_memo(
    n : int,
    cache : Dict[int, int]
    ) -> int:
    
    """Calculate n th fibonacci number
    with 'memoization' method (top-down approach).
    

    Parameters
    ----------
    n : int
        n th of fibonacci
    cache : Dict[int, int]
        Storage saving already calculated fib number

    Returns
    -------
    int
        n th fib number
    """
    
    ## if n th number is in cache, return it
    if n in cache:
        return cache[n]
    
    if n <= 2:
        cache[n] = 1
    else:
        cache[n] = fib_memo(n - 1, cache) + fib_memo(n - 2, cache)    
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}

    return fib_memo(n, fib_cache)

# 테스트
print(fib(10))
print(fib(50))
print(fib(100))

def fib_tab(n : int):
    """Calculate n th fibonacci number 
    with 'tabulation' method (bottom-up approach).

    Parameters
    ----------
    n : int
        n th of fibonacci
    """
    
    table = {1 : 1, 2 : 1}
    for i in range(3, n + 1):
        table[i] = table[i - 1] + table[i - 2]        

    return table[n]

# 테스트
print(fib_tab(10))
print(fib_tab(56))
print(fib_tab(132))