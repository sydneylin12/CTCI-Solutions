# Problem 15 - given a stream of infinite elements, pick one at random
import random

class Stream():
    def __init__(self, data):
        self.data = data
        self.state = self.data
        self.next = self.byTwo

    def nextInt(self):
        self.state += 1
        self.data = self.state

    def byTwo(self):
        self.state += 2
        self.data = self.state

# s = a stream
def randomElement(s):
    initial = (s.state, s.data)

    while True:
        temp = random.randint(1, 10000)
        if(temp < 10):
            break
        else:
            s.next()
    
    # Reset the stream 
    temp = s.data
    s.state = initial[0]
    s.data = initial[1]
    return temp

stream = Stream(1)
#for i in range(10):
#    print(stream.data)
#    stream.next()

for i in range(100):
    print(randomElement(stream))
    