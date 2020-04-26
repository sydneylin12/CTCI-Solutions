# Compute running median of a sequence of numbers

# MEDIAN NEEDS TO BE SORTED!!
# Could also be done using a PQ
def get_running_medians(arr):

    if not arr:
        return []

    ret = []
    current = []
    head = 0
    tail = 0

    for i in arr:
        # First element
        if not current:
            ret.append(i)
            current.append(i)

        # Non first element
        else:
            
            # Add to start
            if i < current[head]:
                current = [i] + current
                head += 1

            # Append largest element to end
            elif i > current[tail]:
                current.append(i)
                tail += 1

            # Insert element in middle of list
            else:
                for j in range(len(current)):
                    if current[j] > i:
                        current.insert(j - 1, i)
                        # Tail is moved with an insertion
                        tail += 1
                        break

            # Even list
            if len(current) % 2 == 0:

                # Calculate 2 median indices
                mid1 = int(len(current)/2)
                mid2 = mid1 - 1
                n = (current[mid1] + current[mid2]) / 2
                
                # Cast to handle test cases
                if n.is_integer():
                    n = int(n)

                ret.append(n)

            # Odd list
            else:
                mid = int((len(current) - 1) / 2)
                ret.append(current[mid])

    return ret


assert not get_running_medians(None)
assert not get_running_medians([])
assert get_running_medians([2, 5]) == [2, 3.5]
assert get_running_medians([3, 3, 3, 3]) == [3, 3, 3, 3]
assert get_running_medians([2, 1, 5, 7, 2, 0, 5]) == [2, 1.5, 2, 3.5, 2, 2, 2]