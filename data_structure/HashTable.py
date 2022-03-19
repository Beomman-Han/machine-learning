## Simple hash functions
from typing import Annotated


def hash_function_remainder(
    key : int,
    array_size : int
    ) -> int:
    """Hash function with remainder value

    Parameters
    ----------
    key : int
        Key value for hashing
    array_size : int
        Range of the result of hash function

    Returns
    -------
    int
        Hashing value (remainder from key / array_size)
    """
    
    return key % array_size

from dataclasses import dataclass  ## FIXME find...

@dataclass
class ValueRange:
    min: float
    max: float


def hash_function_multiplication(
    key : int,
    array_size : int,
    a : Annotated[float, ValueRange(0.0, 1.0)]
    ) -> int:
    
    """Hash function with multiplication

    Parameters
    ----------
    key : int
        Key value for hashing
    array_size : int
        Range of the result of hash function
    a : float (0.0 ~ 1.0)
        Specific value for hashing

    Returns
    -------
    int
        Hashing value
    """
    
    return int(array_size * ((a * key) - int(a * key)))


if __name__ == '__main__':
    ## test hash_function_remainder
    print(hash_function_remainder(40, 200))
    print(hash_function_remainder(120, 200))
    print(hash_function_remainder(788, 200))
    print(hash_function_remainder(2307, 200))
    print()
    
    ## test hash_function_multiplication
    print(hash_function_multiplication(40, 200, 0.61426212))
    print(hash_function_multiplication(120, 200, 0.61426212))
    print(hash_function_multiplication(788, 200, 0.61426212))
    print(hash_function_multiplication(2307, 200, 0.61426212))
    print()
    
    ## test python hash function
    print(hash(12345))
    print(hash(12345))
    print(hash(12346))
    
    print(hash(15.1234))
    print(hash(15.1234))
    print(hash(81.1234))

    # print(hash("파이썬"))
    # print(hash("파이썬"))
    # print(hash("자바"))
    
    print(hash('파이썬'))
    print(hash('파이썬'))
    print(hash('자바'))