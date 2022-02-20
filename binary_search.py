def binary_search(element, some_list):
    # 코드를 작성하세요.
    element_idx = None
    upper = len(some_list) - 1
    lower = 0
    while True:
        index = ( upper + lower ) // 2
        if some_list[index] == element:
            element_idx = index
            break
        if upper <= lower:  ## break condition (** consider carefully!)
            break

        if some_list[index] > element:
            upper = index - 1
        else:
            lower = index + 1

    return element_idx
    
print(binary_search(2, [2, 3, 5, 7, 11]))
print(binary_search(0, [2, 3, 5, 7, 11]))
print(binary_search(5, [2, 3, 5, 7, 11]))
print(binary_search(3, [2, 3, 5, 7, 11]))
print(binary_search(11, [2, 3, 5, 7, 11]))