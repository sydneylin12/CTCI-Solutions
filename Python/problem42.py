# Given a list of integers S and a target K, write a function that returns a subset of S that adds to K
# Can have duplicates
# All positive numbers
# My solution - horrible exponential runtime

def subsetSum(arr, k):
    if not arr:
        return []

    if k - arr[0] == 0:
        return [arr[0]]

    if len(arr) > 1:
        incl = [arr[0]] + subsetSum(arr[1:], k - arr[0])
        excl = subsetSum(arr[1:], k)

        if sum(incl) == k:
            return incl
        elif sum(excl) == k:
            return excl
        else:
            return []
    else:
        return []

def sum(arr):
    sum = 0
    for i in arr:
        sum += i
    return sum

assert not subsetSum([], 1)
assert subsetSum([12, 1, 61, 5, 9, 2], 24) == [12, 1, 9, 2]
assert subsetSum([12, 1, 61, 5, 9, 2], 61) == [61]
assert subsetSum([12, 1, 61, 5, -108, 2], -106) == [-108, 2]