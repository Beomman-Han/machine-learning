import sys, os

from algorithm_paradigm.divide_conquer.quick_sort import quicksort
# print(os.getcwd())
# sys.path.append(os.getcwd())
# print(sys.path)

from algorithm_paradigm import *

def test_quicksort():
    
    list1 = [5,4,2,6,1,6,8,2,6,8,31,2,6]
    quicksort(list1)
    print(list1)    
    
    return

if __name__ == '__main__':
    
    def main():
        test_quicksort()
        return

    main()