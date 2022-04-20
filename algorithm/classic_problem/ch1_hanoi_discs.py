from typing import TypeVar, Generic, List
T = TypeVar('T')
import sys

class Stack(Generic[T]):  ## Generic??
    """Stack implementation with python list"""

    def __init__(self, name: str) -> None:
        self.name = name
        self._container: List[T] = []

    def push(self, item: T) -> None:
        self._container.append(item)
        return

    def pop(self) -> T:
        if len(self._container) == 0:
            raise IndexError(f'Already empty')
        item = self._container[-1]
        del self._container[-1]
        return item
    
    def __repr__(self) -> str:
        return repr(self._container)


def move_discs(_from: Stack[int], _to: Stack[int], _temp: Stack[int], disc: int) -> None:
# def move_discs(_from: Stack[int], _to: Stack[int], _temp: Stack[int]) -> None:

    if disc == 1:
    # if len(_from._container) == 1:
        print(f'Move disc from {_from.name} to {_to.name}')
        _to.push(_from.pop())
    else:
        move_discs(_from, _temp, _to, disc - 1)
        move_discs(_from, _to, _temp, 1)
        move_discs(_temp, _to, _from, disc - 1)
    # move_discs(_from, _temp, _to)

    return

if __name__ == '__main__':
    def run_hanoi():
        num_discs = 4
        tower_a: Stack[int] = Stack('A')
        tower_b: Stack[int] = Stack('B')
        tower_c: Stack[int] = Stack('C')
        
        for i in range(1, num_discs + 1):
            tower_a.push(i)

        #print(tower_a, tower_b, tower_c)
        move_discs(tower_a, tower_c, tower_b, num_discs)
        print(tower_a, tower_b, tower_c)


    def main():
        run_hanoi()

    main()