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
        if(self.length > self.size):
            del self.orders[0]
        else:
            self.length += 1

    # Get ith to last element in O(1)
    def get_last(self, i):
        if i > self.length:
            return -1
        return self.orders[self.length - i]


log = Log(10)
for i in range(20):
    log.record(i)
print(log.get_last(3))
