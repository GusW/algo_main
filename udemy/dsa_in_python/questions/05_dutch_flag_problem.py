def sort_tripple(arr: list[int], pivot: int = 1) -> list[int]:

    i = j = 0
    k = len(arr) - 1

    while j <= k:
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j += 1
        elif arr[j] > pivot:
            arr[j], arr[k] = arr[k], arr[j]
            k -= 1
        else:
            j += 1

    return arr


print(sort_tripple([1, 2, 0, 0, 2, 1, 1]))
