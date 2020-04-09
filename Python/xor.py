
# Use for dereferencing
import _ctypes

# XOR node class
class Node:
    def __init__(self, data):
        self.data = data
        # Both is a pointer, not a node
        self.both = get_pointer(None)

# Memory saving XOR linked list
# DCP problem 6
class ListXOR:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        # Need to add this list bc python auto memory management
        self.ls = []
    
    def add(self, data):
        print("Adding: " + str(data))
        if self.tail is None:
            temp = Node(data)
            self.ls.append(temp)
            self.head = self.tail = temp
            self.length += 1
            return

        # Create a new node
        next = Node(data)

        # Append it so IT DOES NOT GET THE MEMORY REALLOCATED
        self.ls.append(next)

        previousPtr = self.tail.both ^ get_pointer(None)

        # Current both only had null pointer so XORing 2 nulls will be 0
        if previousPtr == 0: 
            self.tail.both = get_pointer(None) ^ get_pointer(next)
        else:
            self.tail.both = previousPtr ^ get_pointer(next)

        # Set new tail node pointer to previous (tail) and null (right side)
        next.both = next.both ^ get_pointer(self.tail) 
        self.tail = next
        self.length += 1

    # Print out the linked list by traversing it
    def traverse(self):
        current = self.head
        previous = None
        print("[", end = "")
        while current != None:
            print(current.data, end = "")
            temp = current
            current = dereference_pointer(get_pointer(previous) ^ current.both)
            previous = temp
            if current is not None:
                print(", ", end = "")
        print("]")

    # Reverse traversal of a linked list
    def reverse(self):
        current = self.tail
        previous = None
        print("[", end = "")
        while current != None:
            print(current.data, end = "")
            temp = current
            current = dereference_pointer(get_pointer(previous) ^ current.both)
            previous = temp
            if current is not None:
                print(", ", end = "")
        print("]")

    # Get node at index i
    def get(self, idx):
        if idx >= self.length:
            print("Index out of range!")
            return None

        current = self.head
        previous = None
        for _ in range(idx):
            temp = current
            current = dereference_pointer(get_pointer(previous) ^ current.both)
            previous = temp
        return current.data

# Test method
def main():
    l = ListXOR()
    l.add(1)
    l.add(2)
    l.add(3)
    l.add(4)
    l.add(5)
    l.add(6)
    l.add(11)
    l.add(22)
    l.add(33)
    l.add(44)
    l.add(55)
    l.add(66)
    l.traverse()
    l.reverse()
    print(l.get(3))
    print(l.get(11))

def get_pointer(obj):
    return id(obj)

def dereference_pointer(id):
    return _ctypes.PyObj_FromPtr(id)

if __name__ == "__main__":
    main()