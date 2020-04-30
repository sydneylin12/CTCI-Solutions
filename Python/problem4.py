# Daily coding problem 4
# Find first missing positive inteeger
# O(n) runtime and O(1) space complexity

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def missingPositive(arr):
    i = 0
    # Iterate through the array and swap elements to their index
    # EX: element 2 at index 2
    while(i < len(arr)):
        
        # Value at index i
        current = arr[i]

        # If the value is index-able
        if(current > 0 and current <= len(arr)):

            # If the current number is not in its place
            # EX: current = 4 should be at index 3
            if(current != arr[current - 1]):
                swap(arr, i, arr[i] - 1)
            else:
                i += 1

        # If the value is not index-able
        else:
            i += 1
    
    # End swap loop
    i = 0
    while(i < len(arr) and arr[i] == i + 1):
        i  += 1
    
    return i + 1

assert missingPositive([3, 4, -1, 1]) == 2
assert missingPositive([1, 2, 0]) == 3
assert missingPositive([1, 2, 5]) == 3
assert missingPositive([1]) == 2
assert missingPositive([-1, -2]) == 1
assert missingPositive([]) == 1