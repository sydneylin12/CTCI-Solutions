# Arithmetic binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def solveTree(root):
    if not root:
        return 0
    
    # Leaf node
    elif root.left == None and root.right == None:
        return int(root.data)

    else:
        if root.data == "+":
            return solveTree(root.left) + solveTree(root.right)

        elif root.data == "-":
            return solveTree(root.left) - solveTree(root.right)

        elif root.data == "/":
            return solveTree(root.left) / solveTree(root.right)

        elif root.data == "*":    
            return solveTree(root.left) * solveTree(root.right)


d = Node("3")
e = Node("2")
f = Node("4")
g = Node("5")

b = Node("+")
b.left = d
b.right = e

c = Node("+")
c.left = f
c.right = g

a = Node("*")
a.left = b
a.right = c

solveTree(a)


assert solveTree(a) == 45
assert solveTree(c) == 9
assert solveTree(b) == 5
assert solveTree(d) == 3