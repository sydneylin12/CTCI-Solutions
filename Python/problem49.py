# Find maximum sum of any contigous subarray
# Do this in O(n) time

# Kadane's algorithm
def maxSub(arr):
    maxSoFar = 0
    maxEndingHere = 0

    for i in range(len(arr)):
        maxEndingHere += arr[i]
        print((maxSoFar, maxEndingHere))

        # If the max ending at arr[i] is negative (illegal solution)
        # Everything before this is USELESS
        if maxEndingHere < 0:
            maxEndingHere = 0

        # If the max ending at arr[i] is the largest in the entire loop/algorithm
        # Set new max
        if maxSoFar < maxEndingHere:
            maxSoFar = maxEndingHere

    return maxSoFar

assert maxSub([34, -50, 42, 14, -5, 86]) == 137
assert maxSub([-5, -1, -8, -9]) == 0