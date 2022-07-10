def is_palindrome(text: str) -> bool:
    left, right = 0, len(text) - 1
    while left < right:
        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


text1 = "madam"
print(is_palindrome(text1))

text2 = "racecar"
print(is_palindrome(text2))

text3 = "thisisnotapalindrome"
print(is_palindrome(text3))
