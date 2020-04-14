# Problem 1 - two sum
# O(n) runntime and space complexity

def twoSum(k, arr):
    map = {}
    for val in arr:
        if val in map.values():
            return True
        else:
            map[val] = k - val
    return False

arr = [10, 15, 3, 7]
k = 1
print(twoSum(k, arr))
        