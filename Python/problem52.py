# Implement a least recently used cache
# Initialize with size n
# Methods:

'''
set(k, v) - set key to value, if there are already n items in cache then remove least recently used item
get(k) - get the value at key
'''

class Node:
    def __init__(self, key, data):
        self.key = key
        self.data = data
        self.next = None
        self.previous = None

class Cache:

    # Consists of a doubly linked list and a hashmap
    def __init__(self, n):
        self.size = n
        self.length = 0
        self.head = None
        self.tail = None
        self.map = dict()

    def set(self, k, v):
        # Remove last recently used item
        if self.length + 1 > self.size:
            del self.map[self.tail.key]
            self.tail = self.tail.next

        new = Node(k, v)
        self.map[k] = new

        if self.length == 0:
            self.head = new
            self.tail = self.head 
            self.length += 1

        else:
            self.head.next = new
            new.previous = self.head
            self.head = new
            self.length += 1
        
    # Get item with key and move to most recently used
    def get(self, k):
        if k not in self.map.keys():
            return None

        # Get the node holding the item
        temp = self.map[k]

        if self.head == temp:
            return temp.data

        # Only need to update tail pointer to next node
        elif self.tail == temp and self.length > 1:
            self.tail = temp.next

        # Update links around current node
        else:
            temp.previous.next = temp.next
            temp.next.previous = temp.previous

        # Update head no matter what
        temp.previous = self.head
        self.head.next = temp
        temp.next = None
        self.head = temp

        return temp.data

    def print(self):
        current = self.tail
        while current:
            print(current.data, end = " ")
            current = current.next
        print()

c = Cache(3)
c.set("V", "Vanilla")
c.set("C", "Chocolate")
c.set("S", "Strawberry")
c.set("P", "Pound")
c.set("X", "Xanthan")
print(c.get("S"))
print(c.get("X"))
c.print()

lru = Cache(3)

assert not lru.get("a")
lru.set("a", 1)
assert lru.get("a") == 1
lru.set("b", 2)
lru.set("c", 3)
lru.set("d", 4)
lru.set("e", 5)
lru.set("a", 1)
assert lru.get("a") == 1
assert not lru.get("b")
assert lru.get("e") == 5
assert not lru.get("c")