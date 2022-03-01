from typing import List

def trapping_rain_v2(
    buildings: List[int]
    ) -> int:
    """Calculate the amount of rain
    trapped between buildings 
    for reducing time complexity
    compared to trapping_rain implementation.
    
    Ex) [3, 0, 0, 2, 0, 4] : the total number of '~' ('~' representing rain)

         |             |
    |    |        |~~~~|
    |  | |   =>   |~~|~|
    |  | |        |~~|~|
    ------        ------
                   ^
                   
    ** brute and force method
    For all index of input list, calculate the amount of rain
    Think about how to determine each amount of rain at an index

    Time Complexity
    ---------------
    O(n^2)
        n : length of buildings
    
    Parameters
    ----------
    buildings : List[int]
        list of the height of buildings

    Returns
    -------
    int
        the amount of rain
    """
    
    total_rain = 0
    for i in range(1, len(buildings) - 1):
        
        left_max = max(buildings[:i])
        right_max = max(buildings[i+1:])
        
        rain = min(left_max, right_max) - buildings[i]
        if rain < 0:
            rain = 0
        total_rain += rain
    return total_rain

def trapping_rain(
    buildings: List[int]
    ) -> int:
    """Calculate the amount of rain 
    trapped between buildings.
    
    Ex) [3, 0, 0, 2, 0, 4] : the total number of '~' ('~' representing rain)
    
             |             |
        |    |        |~~~~|
        |  | |   =>   |~~|~|
        |  | |        |~~|~|
        ------        ------
        
    ** (brute force) for every floor of all buildings, calculate the amount of rain **   

    Time Complexity
    ---------------
    O(n^2 * m)
        n : length of buildings
        m : max element of buildings

    Parameters
    ----------
    buildings : List[int]
        list of the height of buildings

    Returns
    -------
    int
        the amount of rain
    """

    total_rain = 0
    for i in range(len(buildings)):
        ## for every floor of buildings[i]
        for j in range(1, buildings[i]+1):
            ## look all other buildings
            for k in range(i+1, len(buildings)):
                ## condition that rain could be trapped at jth floor
                if j <= buildings[k]:
                    total_rain += (k - i - 1)
                    break

    return total_rain


if __name__ == '__main__':

    # 테스트
    print(trapping_rain_v2([3, 0, 0, 2, 0, 4]))  ## 4 + 4 + 1 + 1 = 10
    print(trapping_rain_v2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))  ## 1 + 3 + 1 + 1
