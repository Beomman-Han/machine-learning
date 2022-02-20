"""
Time complexity practice
"""

## Time complexity : O(1)
def print_first(my_list):
    print(my_list[0])
    return

## Time complexity : O(n)
def print_each(my_list):
    for i in range(len(my_list)):
        print(my_list[i])
    return

def print_each_2(my_list):
    for i in range(len(my_list) // 2):
        print(my_list[i])
    return

def print_each_3(my_list):
    for i in range(len(my_list)):
        print(my_list[i])
    
    for i in range(len(my_list)):
        print(i)
        
    for i in range(len(my_list)):
        print(my_list[0])
    return

## Time complexity : O(n^2)
def print_pairs(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            print(my_list[i], my_list[j])
    return

## Time complexity : O(n^3)
def print_three_times(my_list):
    for i in range(len(my_list)):
        for j in range(len(my_list)):
            for k in range(len(my_list)):
                print(my_list[i], my_list[j], my_list[k])
                
## Time complexity : O(lg n)
def print_powers_of_two(n):
    i = 1
    while n >= i:
        print(i)
        i *= 2
    return

## Time complexity : O(n lg n)
def print_powers_of_two_repeatedly(n):
    for i in range(n):
        j = 1
        while j <= n:
            print(i, j)
            j *= 2
    return

def print_powers_of_two_pepeatedly_2(n):
    i = 1
    while i <= n:
        for j in range(n):
            print(i, j)
        i *= 2
    return

