"""
1. Write another function which returns nth number of fibonacci (your own implementation)
    Compare correctness and ...
2. ??
3. Write function solving honoi problem regardless of the number of towers
4. Encrypt and decrypt image data
"""
from tkinter import NE
from ch1_fibonacci import fib1, fib2, fib4, fib5, fib6

def fibonacci(n: int) -> int:
    """fibonacci own implementation"""
    if n < 2:
        return n

    last, next = 0, 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

from typing import Iterator, List, TypeVar
T = TypeVar('T')

# def Wrapping(cls: type[int]) -> type[int]:

#     class Wrapper(object):
#         def __init__(self, n: int) -> None:
#             self._int = cls(n)

#         def __next__(self):
#             pass

#         def __getitem__(self):
#             pass

#     return Wrapper

# @Wrapping
class NewInt(int):  ## implementation by inheritance ... -> Wrapper class??
    """
    Example
    -------
    >>> new_int = NewInt(20)
    >>> print(new_int)
    10100
    >>> print(new_int[2])
    1
    >>> print(new_int[3])
    0
    >>> for bit in new_int:
    ...     print(bit)

    1
    0
    1
    0
    0
    """

    def __init__(self, n: int) -> None:
        self._int = n
        self.bit_list = self._to_bit_list()
        self._curr = 0

    def _to_bit_list(self) -> List[int]:
        """transform self._int to bit list
            20 -> [1,0,1,0,0]

        Returns
        -------
        List[int]
            list containing bit
        """

        _int = self._int
        bit, bit_length = 1, 0
        while bit < _int:
            bit *= 2
            bit_length += 1

        bit_list = []
        for i in range(bit_length):
            if _int // (2 ** (bit_length - i - 1)):
                bit_list.append(1)
                _int -= 2 ** (bit_length - i - 1)
            else:
                bit_list.append(0)
        return bit_list
    
    def __iter__(self) -> 'NewInt':
        self._curr = 0
        return self
    
    def __next__(self) -> int:
        if len(self.bit_list) <= self._curr:
            raise StopIteration
        else:
            item = self.bit_list[self._curr]
            self._curr += 1
            return item
    
    def __getitem__(self, idx: int) -> int:
        return self.bit_list[idx]

    def __str__(self) -> str:
        bit_string = ''
        for bit in self.bit_list:
            bit_string += str(bit)
        return bit_string
    
    def __add__(self, n: T) -> T:
        if isinstance(n, NewInt):
            newint = NewInt(self._int + n._int)
        else:
            ## int case
            newint = NewInt(self._int + n)
        return newint

from ch1_hanoi_discs import Stack

def hanoi_basic(_from: Stack[int], _to: Stack[int], _temp: Stack[int], num_disc: int) -> None:
    """solve basic hanoi problem where A, B, C towers"""
    if num_disc == 1:
        _to.push(_from.pop())
        return

    hanoi_basic(_from, _temp, _to, num_disc-1)
    hanoi_basic(_from, _to, _temp, 1)
    hanoi_basic(_temp, _to, _from, num_disc-1)

    return

## FIXME
def hanoi_advanced(_from: Stack[int], _to: Stack[int], num_disc: int) -> None:
    """solve advanced hanoi problem where the number of towers are above 3"""
    if num_disc == 1:
        _to.push(_from.pop())



    return

from secrets import token_bytes
from typing import Tuple

# def make_random_byte(length: int):
def make_random_key(length: int) -> int:
    """make random key which of the length is determined"""
    
    random_byte = token_bytes(length)
    # print(random_byte)

    return int.from_bytes(random_byte, "big")

def make_bytes(file_path: str) -> bytes:

    file = open(file_path, 'rb')
    data = file.read()
    file.close()

    return data

def encrypt_file(file_path: str) -> Tuple[int, int]:
    """encrypt data"""

    byte_data = make_bytes(file_path)
    data_key = int.from_bytes(byte_data, "big")
    dummy_key = make_random_key(len(byte_data))

    encrypted_key = data_key ^ dummy_key  ## XOR operation

    return (encrypted_key, dummy_key)

def decrypt_file(encr_key: int, dummy_key: int, file_path: str) -> None:
    """decrypt data to file"""
    
    data_key = encr_key ^ dummy_key
    data_bytes = data_key.to_bytes((data_key.bit_length() + 7 ) // 8, "big")  ## ?? data_key.bit_length() + 7 // 8 ???

    file = open(file_path, 'wb')
    file.write(data_bytes)
    file.close()

    return

def main():
    
    ## test fibonacci functions
    #print(fibonacci(100))

    ## test newint class
    # newint = NewInt(20)
    # print(newint)
    # newint2 = NewInt(30)
    # print(newint2)
    # print(newint + newint2)
    # for bit in newint:
    #     print(bit)
    # for bit in newint:
    #     print(bit)
    encrypted_key, dummy_key = encrypt_file('./image.jpg')
    print(encrypted_key, dummy_key)
    decrypt_file(encrypted_key, dummy_key, './image_decrypted.jpg')
    
    return

main()