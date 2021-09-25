from typing import List, Any


def quicksort(arr: List[Any]):

    def quicksort_helper(arr: List[Any], left: int, right: int):
        print(arr, left, right)
        if left >= right:
            return

        pivot = left
        for i in range(left + 1, right + 1):
            if arr[i] <= arr[pivot]:
                pivot += 1
                arr[i], arr[pivot] = arr[pivot], arr[i]

        arr[left], arr[pivot] = arr[pivot], arr[left]

        quicksort_helper(arr, left, pivot - 1)
        quicksort_helper(arr, pivot + 1, right)

    return quicksort_helper(arr, 0, len(arr) - 1)


def mergesort(arr: List[Any]):
    if len(arr) <= 1:
        return

    m = len(arr) // 2
    larr = arr[:m]
    rarr = arr[m:]

    mergesort(larr)
    mergesort(rarr)

    i = j = k = 0

    while i < len(larr) and j < len(rarr):
        if larr[i] <= rarr[j]:
            arr[k] = larr[i]
            i += 1
        else:
            arr[k] = rarr[j]
            j += 1
        k += 1

    while i < len(larr):
        arr[k] = larr[i]
        i += 1
        k += 1

    while j < len(rarr):
        arr[k] = rarr[j]
        j += 1
        k += 1

arr = list(range(20))[::-1]
print(arr)
mergesort(arr)
print(arr)
