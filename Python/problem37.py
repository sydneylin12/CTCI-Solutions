# Create a power set of a set
# Total elements = 2^n
# Needed G4G

def powerSet(arr):
    if not arr:
        return [set()]

    setSize = pow(2, len(arr))
    ret = []

    maxLen = 0
    for i in range(setSize):
        temp = str(bin(i))[2:]
        if len(temp) > maxLen:
            maxLen = len(temp)
    
    formatter = "{:0" + str(maxLen) + "d}"

    # Loop for power set size
    for i in range(setSize):
        temp = str(bin(i))[2:]
        binary = formatter.format(int(temp))

        # Loop for actual set size
        newSet = set()
        for j in range(len(arr)):
            if binary[j] == "1":
                newSet.add(arr[j])

        ret.append(newSet)
    return ret

assert powerSet([]) == [set()]
assert powerSet([1]) == [set(), {1}]
assert powerSet([1, 2]) == [set(), {2}, {1}, {1, 2}]
assert powerSet([1, 2, 3]) == [set(), {3}, {2}, {2, 3}, {1}, {1, 3}, {1, 2}, {1, 2, 3}]
assert powerSet([1, 2, 3, 4]) == [set(), {4}, {3}, {3, 4}, {2}, {2, 4}, {2, 3}, {2, 3, 4}, {1}, {1, 4}, {1, 3}, {1, 3, 4}, {1, 2}, {1, 2, 4}, {1, 2, 3}, {1, 2, 3, 4}]