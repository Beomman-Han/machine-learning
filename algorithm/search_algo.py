from typing import Iterable, TypeVar, Sequence, Any, Protocol


T = TypeVar('T')

def linear_search(
    iterable : Iterable[T],
    key : T
    ) -> bool:
    
    for item in iterable:
        if item == key:
            return True
    return False

C = TypeVar('C', bound='Comparable')

class Comparable(Protocol):
    def __eq__(self, other : Any) -> bool:
        ...
    
    def __lt__(self : C, other : C) -> bool:
        ...
        
    def __gt__(self : C, other : C) -> bool:
        return (not self < other) and self != other
    
    def __le__(self : C, other : C) -> bool:
        return self < other or self == other
    
    def __ge__(self : C, other : C) -> bool:
        return not self < other

def binary_search(sequence : Sequence[C], key : C) -> bool:
    
    low = 0
    high = len(sequence) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True

    return False

if __name__ == '__main__':
    print(linear_search([1, 5, 15, 15, 15, 15, 20], 5))
    print(binary_search(['a', 'd', 'e', 'f', 'z'], 'f'))
    print(binary_search(['john', 'mark', 'ronald', 'sarah'], 'sheila'))