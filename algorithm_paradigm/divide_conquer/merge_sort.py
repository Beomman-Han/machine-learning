## merge function implementation for merge sort

def merge(list1: list, list2: list) -> list:
    """Merge from two sorted list to sorted list

    Parameters
    ----------
    list1 : _type_
        sorted list 1
    list2 : _type_
        sorted list 2
    
    Returns
    -------
    list
        merged sorted list
    """
    
    merged = []
    idx1, idx2 = 0, 0
    while idx1 < len(list1) or idx2 < len(list2):
        if idx1 >= len(list1):
            merged += list2[idx2:]
            break
                
        if idx2 >= len(list2):
            merged += list1[idx1:]
            break
        
        if list1[idx1] <= list2[idx2]:
            merged.append(list1[idx1])
            idx1 += 1
        else:
            merged.append(list2[idx2])
            idx2 += 1

    return merged

# 테스트
print(merge([1],[]))
print(merge([],[1]))
print(merge([2],[1]))
print(merge([1, 2, 3, 4],[5, 6, 7, 8]))
print(merge([5, 6, 7, 8],[1, 2, 3, 4]))
print(merge([4, 7, 8, 9],[1, 3, 6, 10]))