from tkinter import N
from typing import Dict, Generator
import time

global n_recursive
n_recursive = 0
def fib1(n: int) -> int:
    """fibonacci with recursive way"""
    # if n == 1:
    #     return 0
    # elif n == 2:
    #     return 1
    global n_recursive
    n_recursive += 1
    # print(f'fib1: {N}')
    if n < 2:
        return n
    return fib1(n - 1) + fib1(n - 2)

global n_memo
n_memo = 0
memo: Dict[int, int] = {0: 0, 1: 1}

def fib2(n: int) -> int:
    """fibonacci with memoization"""
    global n_memo
    n_memo += 1
    if n not in memo.keys():
        #return memo[n - 1] + memo[n - 2]
        memo[n] = fib2(n - 1) + fib2(n - 2)
    #     return memo[n]
    # else: 
    return memo[n]

from functools import lru_cache

global n_lru_cache
n_lru_cache = 0

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    """fibonacci with memoization (lru_cache decorator)"""
    global n_lru_cache
    n_lru_cache += 1
    if n < 2:
        return n
    return fib4(n - 1) + fib4(n - 2)

def fib5(n: int) -> int:
    """fibonacci with classic way"""
    if n == 0: return n
    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, last + next  ## technique w/o 'temp' variable
    return next

def fib6(n: int) -> Generator[int, None, None]:
    """fibonacci with generator"""
    yield 0
    if n == 1: yield 1
    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, last + next
        yield next


if __name__ == "__main__":
    def run_fib():
        # print(time.ctime())
        # print(fib4(20))
        # print(time.ctime())
        # print(n_lru_cache)

        # print(time.ctime())
        # print(fib2(20))
        # print(time.ctime())
        # print(n_memo)
        
        """
        iter = iter(fib6(20))  ## generator object 
        while True:
            try:
                next(iter)
            except IterationStop:
                break        
        """
        # print(fib6(20))
        # print(iter(fib6(20)))
        for i in fib6(50):
            print(i)
        
        return

    run_fib()