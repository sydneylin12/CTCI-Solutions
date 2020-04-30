# Out of order array - count number of inversions
# Have to do this using merge sort
# Gotta figure out how to do this

def inversions1(arr):
    inv = 0
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if arr[i] > arr[j] and i < j:
                inv += 1
    return inv

def merge(arr, brr):
    i = 0
    j = 0

    a, aInversions = arr
    b, bInversions = brr
    inversions = aInversions + bInversions
    merged = []

    # Create a sorted list from 2 sub lists
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            inversions += len(a[i:])
            j += 1
    
    # Cleanup loops
    while i < len(a):
        merged.append(a[i])
        i += 1
    while j < len(b):
        merged.append(b[j])
        j += 1

    return merged, inversions

def mergeSort(arr):
    if not arr or len(arr) == 1:
        return arr, 0

    mid = len(arr) // 2
    merged, inversions = merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))

    return merged, inversions

def inversions(arr):
    _, inversions = mergeSort(arr)
    return inversions

assert inversions([1, 2, 3, 4, 5]) == 0
assert inversions([2, 1, 3, 4, 5]) == 1
assert inversions([2, 4, 1, 3, 5]) == 3
assert inversions([2, 6, 1, 3, 7]) == 3
assert inversions([5, 4, 3, 2, 1]) == 10