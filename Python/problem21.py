# Problem 21
# Find minimum amount of rooms for overlapping classes
# Not sure if this is right

def rooms(arr):

    rooms = 0

    # Get first node from array as a room
    while len(arr) > 1:
        current = arr[0]
        toRemove = []

        # Iterate from 1 to N
        for i in range(1, len(arr)):

            # If there is no overlaps with the currrent room
            # ONLY REMOVE 1 ROOM
            if not overlap(current, arr[i]):
                # Append the room at index i
                toRemove.append(arr[i])
                break
            
                
        # Remove all compatible classes from the list
        for idx in toRemove:
            arr.remove(idx)

        # Slice off the first element (get rid of first class)
        arr = arr[1::]
        rooms += 1

    return rooms

# Helper method runs in O(1)
def overlap(interval1, interval2):

    # interval 1 start is between interval 2 start and end
    if interval1[0]  > interval2[0] and interval1[0] < interval2[1]:
        return True

    # interval 1 end is between interval 2 start and end
    elif interval1[1]  > interval2[0] and interval1[1] < interval2[1]:
        return True

    return False

# 2 conflicts
times = [(30, 75), (0, 50), (60, 150)]
print(rooms(times))

# 5 conflicts
times = [(1, 2), (2, 3), (3, 4), (2, 4), (2, 5), (2, 6), (2, 7)]
print(rooms(times))