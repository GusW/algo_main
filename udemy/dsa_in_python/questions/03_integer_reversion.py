def invert_int(number: int) -> int:
    target = list(str(number))
    left, right = 0, len(target) - 1
    while left < right:
        target[left], target[right] = target[right], target[left]
        left += 1
        right -= 1

    return int("".join(target))


def invert_int_mat(number: int) -> int:
    rev = remainder = 0
    while number > 0:
        number, remainder = divmod(number, 10)
        rev = rev * 10 + remainder

    return rev


num1 = 1234
print(invert_int(num1))
print(invert_int_mat(num1))


num2 = 54379
print(invert_int(num2))
print(invert_int_mat(num2))
