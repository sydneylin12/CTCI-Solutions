# Order an array of RGB colors in linear time and in place

def swapColors(arr):

    if not arr:
        return []

    # Total number of colors in array
    r = 0
    g = 0
    b = 0

    for i in arr:
        if i == "R":
            r += 1
        elif i == "G":
            g += 1
        elif i == "B":
            b += 1

    rIndex = 0
    gIndex = rIndex + r
    bIndex = gIndex + g

    # Keeps track of the current index of each R G B
    currentR = rIndex
    currentG = gIndex
    currentB = bIndex

    for i in range(len(arr)):
        if arr[i] == "R" and i >= rIndex and i < gIndex:
            continue
        elif arr[i] == "G" and i >= gIndex and i < bIndex:
            continue
        elif arr[i] == "B" and i >= bIndex and i < len(arr):
            continue
        else:
            if arr[i] == "R":
                swap(arr, i, currentR)
                currentR += 1
            elif arr[i] == "G":
                swap(arr, i, currentG)
                currentG += 1
            elif arr[i] == "B":
                swap(arr, i, currentB)
                currentB += 1
    return arr

# Swap help method
def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


assert swapColors(['G', 'R']) == ['R', 'G']
assert swapColors(['G', 'B']) == ['G', 'B']
assert swapColors(['B', 'R']) == ['R', 'B']
assert swapColors(['G', 'B', 'R']) == ['R', 'G', 'B']
assert swapColors(['B', 'G', 'R']) == ['R', 'G', 'B']
assert swapColors(['G', 'B', 'R', 'R', 'B', 'R', 'G']) == ['R', 'R', 'R', 'G', 'G', 'B', 'B']