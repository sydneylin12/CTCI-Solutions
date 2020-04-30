# Probelm 18 - Compute max values of each subarray of length K

def maxSubarray(arr, k):
    if len(arr) < k:
        return # Error case

    ret = []
    
    # O(n) because it iterates through the array once
    while True:
        # Breakout case
        if len(arr) < k:
            break

        # Will have K elements in this list
        max = arr[0]
        for i in range(k):
            if arr[i] > max:
                max = arr[i]
        ret.append(max)  

        # Slice first element off
        arr = arr[1::]

    return ret

assert maxSubarray([10, 5, 2, 7, 8, 7], 3) == [10, 7, 8, 8]
assert maxSubarray([5, 2, 1], 2) == [5, 2]