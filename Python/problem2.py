# Problem 2 - all product
# O(n) time and O(1) space with mutable array and division

def allProduct(arr):
    prod = 1
    for val in arr:
        prod *= val
    for i in range(len(arr)):
        arr[i] = int(prod/arr[i])
    return arr

arr = [1, 2, 3, 4, 5]
print(allProduct(arr))
print(allProduct([3, 2, 1]))