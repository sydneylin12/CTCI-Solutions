# Given an array that represents a 2d elevation map
# Suppose it rains and all spots between 2 walls fill up
# Compute how many units of water are trapped in O(n) time and O(1) space

# Could not solve this one... rip

'''
Visualization
3,0,1,3,0,5
Solution: 8


          X
          X
X     X   X
X     X   X
X _ X X _ X


'''

def unitsOfWater(arr):

    # Error case
    if not arr:
        return 0
    
    # Cannot trap water with 1 building
    elif len(arr) <= 2:
        return 0

    # Return total keeper
    result = 0

    left = 0
    right = 0    

    low = 0
    high = len(arr) - 1

    # Iterate through the first thru length
    while low < high:
        if arr[low] < arr[high]:
            if arr[low] > left:
                left = arr[low]
            else:
                result += left - arr[low]
            low += 1
        else:
            if arr[high] > right:
                right = arr[high]
            else:
                result += right - arr[high]
            high -= 1
    return result

# Error cases
assert unitsOfWater([1]) == 0
assert unitsOfWater([2, 1]) == 0

# Actual cases
assert unitsOfWater([2, 1, 2]) == 1
assert unitsOfWater([4, 1, 2]) == 1
assert unitsOfWater([4, 1, 2, 3]) == 3
assert unitsOfWater([3, 0, 1, 3, 0, 5]) == 8
assert unitsOfWater([10, 9, 1, 1, 6]) == 10