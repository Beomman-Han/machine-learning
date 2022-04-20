from random import random
from secrets import token_bytes
from typing import Tuple

def random_key(length: int) -> int:
    tb = token_bytes(length)
    return int.from_bytes(tb, "big")

def encrypt(original: str) -> Tuple[int, int]:
    """
    str -> bytes -> int from dummy bytes(same len) -> int from bytes -> XOR
    """
    original_bytes = original.encode()
    # print(original_bytes)
    # print(len(original_bytes))
    dummy = random_key(len(original_bytes))
    original_key = int.from_bytes(original_bytes, "big")
    print(dummy)
    encrypted = original_key ^ dummy
    print(encrypted)
    return dummy, encrypted

def decrypt(key1: int, key2: int) -> str:
    decrypted = key1 ^ key2
    # print(decrypted)
    # print(bin(decrypted))
    # print(decrypted.bit_length())
    # original_key = decrypted.to_bytes(decrypted)
    # print(original_key)
    original_key = decrypted.to_bytes((decrypted.bit_length() + 7) // 8, "big")  ## + 7 // 8
    # print(original_key)
    return original_key.decode()

def main():
    # print(token_bytes(5))
    # print(random_key(5))
    original = 'classic computer science problems in python'
    # print(len(original))
    print(original)
    dummy, encrypted = encrypt(original)
    print(decrypt(dummy, encrypted))

main()