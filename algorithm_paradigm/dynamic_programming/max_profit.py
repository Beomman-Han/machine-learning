from typing import Dict, List


def max_profit_memo(
    price_list : List[int],
    count : int,
    cache : Dict[int, int]
    ) -> int:
    
    """Calculate max profit of 'count' products.
    'price_list' has price of some count of products.
    
    Ex) [0, 100, 400, 800] - 100 for 1 product, 400 for 2 product, ...
    
    Time Complexity
    ---------------
    O(n)
        n : count
    
    Parameters
    ----------
    price_list : List[int]
        Price table
    count : int
        # of products
    cache : Dict[int, int]
        Storage of max profits
    
    Returns
    -------
    int
        Max profit of 'count' products
    """

    ## memoization
    if count in cache:
        return cache[count]

    ## base case
    if count == 1:
        cache[count] = price_list[count]
        return cache[count]
        
    ## recursive case
    # profits = []  ## high memory usage
    if count < len(price_list):
        # profits.append(price_list[count])
        profit = price_list[count]
    else:
        profit = 0
        
    for i in range(1, count // 2 + 1):
        # profits.append(max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, i, cache))
        profit = max(profit, max_profit_memo(price_list, count - i, cache) + max_profit_memo(price_list, i, cache))
    
    # return max(profits)
    return profit
    
def max_profit(price_list, count):
    max_profit_cache = {}

    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))
