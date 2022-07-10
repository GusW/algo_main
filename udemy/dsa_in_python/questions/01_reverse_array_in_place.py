from typing import Any


def reverse(arr: list[Any]) -> list[Any]:
    left, right = 0, len(arr) - 1
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(reverse(list1))

list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(reverse(list2))
