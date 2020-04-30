# Max stack

class MaxStack():
    def __init__(self):
        self.elements = []
        self.maxElements = []

    def isEmpty(self):
        return len(self.elements) == 0

    # O(1)
    def push(self, data):

        # Edge case for empty stack
        if self.isEmpty():
            self.elements.append(data)
            self.maxElements.append(data)
            return

        # Put the data on the regular stack top
        self.elements.append(data)
        last = self.maxElements[len(self.maxElements) - 1]
        if data > last:
            self.maxElements.append(data)
        else:
            self.maxElements.append(last)

    # O(1)
    def pop(self):
        # Pop from an empty stack case
        if self.isEmpty():
            return None

        temp = self.elements[len(self.elements) - 1]
    
        # Remove top
        self.elements.pop()
        self.maxElements.pop()
        return temp

    # O(1)
    def max(self):
        if self.isEmpty():
            return None
        return self.maxElements[len(self.maxElements) - 1]


s = MaxStack()
s.push(1)
s.push(3)
s.push(2)
s.push(5)
assert s.max() == 5
s.pop()
assert s.max() == 3
s.pop()
assert s.max() == 3
s.pop()
assert s.max() == 1
s.pop()
assert not s.max()

s = MaxStack()
s.push(10)
s.push(3)
s.push(2)
s.push(5)
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert s.max() == 10
s.pop()
assert not s.max()