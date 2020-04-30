# Create itinerary

def itinerary(arr, start):
    if not arr:
        return []

    ret = []
    # Find the starting point
    for i in arr:
        if i[0] == start:
            ret.append(i[0])
            ret.append(i[1])
            arr.remove(i)
            break

    # Did not have a correct starting point
    if not ret:
        return []

    # Iterable
    i = 0
    while len(arr) > 0:

        # Last element in itinerary
        current = ret[len(ret) - 1]

        # If starting destination is equal to last end destination
        if arr[i][0] == current:
            ret.append(arr[i][1])
            arr.remove(arr[i])
            i = 0
        else:
            if i + 1 > len(arr):
                i = 0
            else:
                i += 1

    return ret


assert itinerary([('SFO', 'HKO'), ('YYZ', 'SFO'), ('YUL', 'YYZ'), ('HKO', 'ORD')], "YUL") == ['YUL', 'YYZ', 'SFO', 'HKO', 'ORD']
assert not itinerary([('SFO', 'COM'), ('COM', 'YYZ')], "YUL")
assert itinerary([('A', 'B'), ('A', 'C'), ('B', 'C'), ('C', 'A')], "A") == ['A', 'B', 'C', 'A', 'C']
