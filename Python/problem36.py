# Find the second largest node
import sys

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# Iterative O(n) time O(n) space
def secondLargest(root):

    # Traverse the tree into a list
    # Cheater method
    '''
    list = traverse(root)
    if len(list) < 2:
        return None

    max = -sys.maxsize
    for i in list:
        if i > max:
            max = i

    secondMax = -sys.maxsize
    for i in list:
        if i > secondMax and i < max:
            secondMax = i

    return Node(secondMax, None, None)
    '''

    stack = []
    stack.append(root)
    max = -sys.maxsize
    maxNode = None
    count = 0

    # while not empty
    while stack:
        curr = stack.pop()
        count += 1
        if curr.data > max:
            max = curr.data
            maxNode = curr

        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)

    # Do it all again
    stack.append(root)
    secondMax = -sys.maxsize
    while stack:
        curr = stack.pop()
        if curr.data > secondMax and curr.data < max:
            secondMax = curr.data
            maxNode = curr

        if curr.left is not None:
            stack.append(curr.left)
        if curr.right is not None:
            stack.append(curr.right)

    if count < 2:
        return None

    return maxNode


# Helper method to traverse and turn into list
def traverse(root):
    if root is None:
        return []

    ret = []
    ret.append(root.data)

    if root.left is not None:
        ret += traverse(root.left)

    if root.right is not None:
        ret += traverse(root.right)

    return ret

def test_0():
    node_a = Node(5, None, None)

    assert not secondLargest(node_a)


def test_1():
    node_a = Node(5, None, None)
    node_b = Node(3, None, None)
    node_c = Node(8, None, None)
    node_d = Node(2, None, None)
    node_e = Node(4, None, None)
    node_f = Node(7, None, None)
    node_g = Node(9, None, None)
    node_a.left = node_b
    node_a.right = node_c
    node_b.left = node_d
    node_b.right = node_e
    node_c.left = node_f
    node_c.right = node_g
    assert secondLargest(node_a).data == 8


def test_2():
    node_a = Node(5, None, None)
    node_b = Node(3, None, None)
    node_d = Node(2, None, None)
    node_e = Node(4, None, None)
    node_a.left = node_b
    node_b.left = node_d
    node_b.right = node_e
    assert secondLargest(node_a).data == 4

test_0()
test_1()
test_2()