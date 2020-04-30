# Problem 16 - Order Log

class Log:
    # Keep the last N orders
    def __init__(self, size):
        self.orders = []
        self.size = size
        self.length = 0

    # Append to the order list in O(1)
    def record(self, order_id):
        self.orders.append(order_id)
        if(self.length + 1 > self.size):
            del self.orders[0]
        else:
            self.length += 1

    # Get ith to last element in O(1)
    def get_last(self, i):
        if i > self.length:
            return -1
        return self.orders[self.length - i]


log = Log(5)
log.record(1)
log.record(2)
assert log.orders == [1, 2]
log.record(3)
log.record(4)
log.record(5)
assert log.orders == [1, 2, 3, 4, 5]
log.record(6)
log.record(7)
log.record(8)
assert log.orders == [4, 5, 6, 7, 8]
assert log.get_last(4) == 5
assert log.get_last(1) == 8
