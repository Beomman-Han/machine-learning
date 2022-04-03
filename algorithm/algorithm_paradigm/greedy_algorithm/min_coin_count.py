from typing import List


def min_coin_count(value : int, coin_list : List[int]) -> int:
    count = 0
    for coin in sorted(coin_list, reverse=True):
        while True:
            value -= coin
            if value >= 0:
                count += 1
            else:
                value += coin
                break
        # count += (value // coin)
        # value %= coin
    
    return count


# 테스트
default_coin_list = [100, 500, 10, 50]
print(min_coin_count(1170, default_coin_list))
print(min_coin_count(1440, default_coin_list))
print(min_coin_count(1700, default_coin_list))
print(min_coin_count(23520, default_coin_list))
print(min_coin_count(32590, default_coin_list))