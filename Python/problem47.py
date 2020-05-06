import sys

# My solution - O(n^2)
def profit(arr):
    if not arr:
        return None
    elif len(arr) < 2:
        return None

    maxProfit = -sys.maxsize

    for i in range(len(arr)):
        min = arr[i]
        for j in range(i + 1, len(arr)):
            if arr[j] - min > maxProfit:
                maxProfit = arr[j] - min
    
    return maxProfit

def profit2(arr):
    if not arr:
        return None
    elif len(arr) < 2:
        return None

    minPrice = arr[0]
    maxDifference = -sys.maxsize

    # O(n) solution using sequential 
    for i in arr[1:]:
        # If we can get a better difference (max price)
        if i - minPrice > maxDifference:
            maxDifference = i - minPrice
        
        # Update smallest value
        if i < minPrice:
            minPrice = i

    return maxDifference


assert profit([9]) == None
assert profit([9, 11, 8, 5, 7, 10]) == 5
assert profit([1, 2, 3, 4, 5]) == 4
assert profit([1, 1, 1, 1, 1]) == 0
assert profit([1, 1, 1, 2, 1]) == 1
assert profit([5, 4]) == -1