# Implement a locking binary tree

class LockableNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right
        self.locked = False

    def lock(self):
        # Already locked
        if self.locked:
            return False

        elif not self.isLockable():
            return False

        self.locked = True
        return True

    def unlock(self):
        # If already unlocked
        if not self.locked:
            return False

        elif not self.isUnlockable():
            return False

        self.locked = False
        return True

    # Helper method to check if a node is lockable
    def isLockable(self):
        # Back out if we get a locked node
        if self.locked == True:
            return False

        # Leaf node case (unlocked)
        elif self.left == None and self.right == None:
            return True

        elif self.left != None and self.right == None:
            return self.left.isLockable()

        elif self.left == None and self.right != None:
            return self.right.isLockable()

        else:
            return (self.left.isLockable() and self.right.isLockable())

    def isUnlockable(self):
        # Back out if we get a locked node
        if self.locked == False:
            return False

        # Leaf node case (unlocked)
        elif self.left == None and self.right == None:
            return True

        elif self.left != None and self.right == None:
            return self.left.isUnlockable()

        elif self.left == None and self.right != None:
            return self.right.isUnlockable()

        else:
            return (self.left.isUnlockable() and self.right.isUnlockable())


class LockingTree:
    def __init__(self):
        self.root = None
        self.size = 0

root = LockableNode("root", None, None)

left = LockableNode("left", None, None)
left.locked = False

right = LockableNode("right", None, None)
right.locked = False

left_left = LockableNode("left.left", None, None)
left_left.locked = True

# Initialize/create the tree
root.left = left
root.right = right
left.left = left_left

'''
        Root
    Left    Right
Left_Left

'''

print(root.isLockable())
print(root.lock())
print(root.unlock())
print(left_left.unlock())
print(root.lock())