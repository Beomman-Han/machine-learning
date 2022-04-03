def is_palindrome(word):
    """check input word is palindrome
    
    Parameters
    ----------
    word: str
        input word
    
    Returns
    -------
    bool
        is word palindrome
    """

    len_word = len(word)
    for i in range(len_word//2):
        if word[i] != word[len_word-i-1]:
            return False
    return True

print(is_palindrome("racecar"))
print(is_palindrome("stars"))
print(is_palindrome("토마토"))
print(is_palindrome("kayak"))
print(is_palindrome("hello"))