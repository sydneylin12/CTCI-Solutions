# Given a preorder and inorder traversal, reconstruct a tree
# Preorder: root, left, right
# Inorder: left, right, root

# Example
'''
Pre
[a, b, d, e, c, f, g]

In
[d, b, e, a, f, c, g]
'''

class Node:
    def __init__(self, data, left = None, right = None):
        self.data = data
        self.left = None
        self.right = None


def constructTree(preorder, inorder):
    if not preorder or not inorder:
        return None

    elif len(preorder) == 1 and len(inorder) == 1:
        print("Base case with root: " + preorder[0])
        return Node(preorder[0])
    
    root = preorder[0]
    idx = inorder.index(root)

    # Inorder is definitely correct
    # Left subtree inorder
    inLeft = inorder[:idx]

    # Right subtree inorder
    inRight = inorder[idx + 1:]

    # Take the root out - already used
    preorder = preorder[1:]
    preIdx = -1

    for i in range(len(preorder)):
        if preorder[i] in inRight:
            preIdx = i
            break

    # Error handling just in case
    if preIdx == -1:
        return None

    preLeft = preorder[:preIdx]
    preRight = preorder[preIdx:]

    print("Root: " + str(root))
    print("InLeft: " + str(inLeft))
    print("InRight: " + str(inRight))
    print("PreLeft: " + str(preLeft))
    print("PreLeft: " + str(preRight))
    print("")

    # Construct node and recursively call
    n = Node(root)
    n.left = constructTree(preLeft, inLeft)
    n.right = constructTree(preRight, inRight)
    return n


tree = constructTree(preorder=['a', 'b', 'd', 'e', 'c', 'f', 'g'], inorder=['d', 'b', 'e', 'a', 'f', 'c', 'g'])
assert tree.data == 'a'
assert tree.left.data == 'b'
assert tree.left.left.data == 'd'
assert tree.left.right.data == 'e'
assert tree.right.data == 'c'
assert tree.right.left.data == 'f'
assert tree.right.right.data == 'g'

tree = constructTree(preorder=['a', 'b', 'd', 'e', 'c', 'g'], inorder=['d', 'b', 'e', 'a', 'c', 'g'])
assert tree.data == 'a'
assert tree.left.data == 'b'
assert tree.left.left.data == 'd'
assert tree.left.right.data == 'e'
assert tree.right.data == 'c'
assert tree.right.right.data == 'g'
