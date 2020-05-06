# Implement a queue using 2 stacks

class StackedQueue:

    def __init__(self):
        self.stack = list()
        self.length = 0

    # Simply push the data onto the top/back of the list/stack
    def enqueue(self, data):
        self.stack.append(data)
    
    def dequeue(self):
        temp = list()
        # Pop everything off but the last one
        while len(self.stack) > 1:
            temp.append(self.stack.pop())

        # Front most item of queue/bottom of stack
        item = self.stack.pop()

        while len(temp) > 0:
            self.stack.append(temp.pop())

        return item

q = StackedQueue()
q.enqueue(1)
assert q.stack == [1]
q.enqueue(2)
assert q.stack == [1, 2]
q.enqueue(3)
assert q.stack == [1, 2, 3]
val = q.dequeue()
assert val == 1
assert q.stack == [2, 3]
val = q.dequeue()
assert val == 2
assert q.stack == [3]