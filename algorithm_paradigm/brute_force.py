from typing import List

def max_product(
    left_cards: List[int],
    right_cards: List[int]
    ) -> int or None:
    """Calculate max product of two int
    from left_cards list and right_cards list.
    If either left_cards or right_cards has no card,
    it returns None for max_product.
    
    Time Complexity
    ---------------
    O(n * m)
        n : length of left_cards
        m : length of right_cards
    
    Parameters
    ----------
    left_cards : List[int]
        left int cards list
    right_cards : List[int]
        right int cards list

    Returns
    -------
    int
        max product from left_cards and right_cards
    """
    
    if len(left_cards) == 0 or len(right_cards) == 0:
        return None
    
    ## initial setting
    max_product = left_cards[0] * right_cards[0]
    for left in left_cards:
        for right in right_cards:
            product = left * right
            if product > max_product:
                max_product = product
        
    return max_product

if __name__ == '__main__':
    
    ## test for max_product
    print(max_product([1, 6, 5], [4, 2, 3]))
    print(max_product([1, -9, 3, 4], [2, 8, 3, 1]))
    print(max_product([-1, -7, 3], [-4, 3, 6]))