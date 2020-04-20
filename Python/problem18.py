# Probelm 18 - Compute max values of each subarray of length K

def maxSubarray(arr, k):
    if len(arr) < k:
        return # Error case
    
    # O(n) because it iterates through the array once
    while True:
        # Breakout case
        if len(arr) < k:
            print("\n")
            return

        # Will have K elements in this list
        max = arr[0]
        for i in range(k):
            if arr[i] > max:
                max = arr[i]
        print(max, end = " ")     

        # Slice first element off
        arr = arr[1::]

# Array with length 6
# Last index for k = 3 would be 4
arr = [10, 5, 2, 7, 8, 7]
maxSubarray(arr, 5)
maxSubarray(arr, 4)
maxSubarray(arr, 3)
maxSubarray(arr, 2)