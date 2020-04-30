# Problem 1 - two sum
# O(n) runntime and space complexity

def twoSum(arr, k):
    map = {}
    for val in arr:
        if val in map.values():
            return True
        else:
            map[val] = k - val
    return False
        
assert not twoSum([], 17)
assert twoSum([10, 15, 3, 7], 17)
assert not twoSum([10, 15, 3, 4], 17)