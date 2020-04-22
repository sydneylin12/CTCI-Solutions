# Problem 20 
# Find the intersection in a linked list in O(m + n) time

class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

    def print(self):
        current = self
        print("[", end = "")
        while current is not None:
            if current.next is not None:
                print(current.data, end = ", ")
            else:
                print(current.data, end = "")
            current = current.next
        print("]")

    def __len__(self):
        length = 0
        current = self
        while current is not None:
            length += 1
            current = current.next
        return length

# Find intersection between 2 linked lists
# O(n + m) time and O(1) space
def intersection(a, b):
    # Edge case
    if a is None or b is None:
        return None

    # Get minimum length of both lists
    lenA = len(a)
    lenB = len(b)
    minLength = min(len(a), len(b))
    currA = a
    currB = b

    # If the lists are uneven size
    if lenA > lenB:
        # Traverse up the first list to the size of the second
        for i in range(lenA - lenB):
            currA = currA.next
        # Traverse up the second list
    else:
        for i in range(lenB - lenA):
            currB = currB.next
        
    currA.print()
    currB.print()

    for i in range(minLength):
        if currA.data == currB.data:
            return currA
        currA = currA.next
        currB = currB.next
    return None
    

first = Node(7, Node(8, Node(10, None)))
second = Node(99, Node(1, Node(8, Node(10, None))))

result = intersection(first, second)
if result is not None:
    print(result.data)