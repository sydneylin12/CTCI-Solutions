# Find and return the non duplicate integer in O(n) time and O(1) space
# Every integer occurs three times except for one
import sys
import numpy as np

def nonDuplicate(arr):

    # O(n) both
    '''
    dict = {}
    for i in arr:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1

    for i in dict:
        if dict[i] == 1:
            return i
    '''

    # Loophole solution with an array with the max integer slots

    # Find max
    max = 0
    for i in arr:
        if i > max:
            max = i

    # Declare array with fixed size
    # Pretty much a dictionary but created with a number of indexes not proportional to input size
    constantSpaceArray = [0] * max

    for i in arr:
        constantSpaceArray[i-1] += 1

    # Return number with value of 1
    for i in range(max):
        if constantSpaceArray[i] == 1:
            return i + 1

    return 0

def nonDuplicateSolution2(arr):
    single = 0
    intSize = 32

    # Constant time because 32 bits in an int
    for i in range(intSize):
        sumPositionBits = 0
        
        # 2 to the power of i
        x = 1 << i
        print(x)

        # Iterate through the array
        for j in range(len(arr)):
            if arr[j] & x:
                sumPositionBits += 1

        if sumPositionBits % 3:
            # Bitwise or equals
            single |= x

    return single


assert nonDuplicate([6, 1, 3, 3, 3, 6, 6]) == 1
assert nonDuplicate([13, 19, 13, 13]) == 19

assert nonDuplicateSolution2([6, 1, 3, 3, 3, 6, 6]) == 1
assert nonDuplicateSolution2([13, 19, 13, 13]) == 19