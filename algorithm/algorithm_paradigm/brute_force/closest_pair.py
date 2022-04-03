from typing import Tuple, List
from math import sqrt

def distance(
    store1: Tuple[int],
    store2: Tuple[int]
    ) -> float:
    """calculate the euclidean distance between two stores

    Parameters
    ----------
    store1 : Tuple[int]
        x, y coordinates of store1
    store2 : Tuple[int]
        x, y coordinates of store2

    Returns
    -------
    float
        euclidean distance
    """
    return sqrt((store1[0] - store2[0]) ** 2 + (store1[1] - store2[1]) ** 2)

def closest_pair(
    coordinates: List[Tuple[int]]
    ) -> List[Tuple[int]] or List:
    """Find the closest pair of 2 stores from multiple store coordinates
    with brute force algorithm

    Time Complexity
    ---------------
    O(n ^ 2)
        n : length of coordinates (input)
        
    Parameters
    ----------
    coordinates : List[Tuple[int]]
        list of multiple store's xy coordinates

    Returns
    -------
    List[Tuple[int]]
        the closest pair of 2 stores
    """
    
    if len(coordinates) < 2:
        return []
    
    ## initial setting
    pairs = [(coordinates[0], coordinates[1])]
    ## prevent duplicates appending
    shortest_dist = distance(coordinates[0], coordinates[1]) + 1
    ## calculate all pair combinations of input list
    for i in range(len(coordinates)):
        for j in range(i+1, len(coordinates)):
            dist = distance(coordinates[i], coordinates[j])
            if dist < shortest_dist:
                pairs = [(coordinates[i], coordinates[j])]
                shortest_dist = dist
            elif dist == shortest_dist:
                pairs.append((coordinates[i], coordinates[j]))
    
    return [*pairs[0]]


if __name__ == '__main__':
        
    # 테스트
    test_coordinates = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    print(closest_pair(test_coordinates))