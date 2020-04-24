# Remove kth from last element in ONE PASS

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

def getList(linkedList):
    current = linkedList
    ret = []
    while current != None:
        ret.append(current.data)
        current = current.next
    return ret

def remove_kth_last(list, k):

    # O(n) solution with O(1) space
    # However this is more than 1 pass
    '''
    current = list
    length = 0
    while current:
        length += 1
        current = current.next
    
    print(length)
    current = list
    for i in range(length - k - 1):
        current = current.next

    current.next = current.next.next
    return list
    '''

    # G4G solution - keep 2 pointers
    # Move 1 ahead by k + 1 steps (to get main pointer to previous node of k)
    # Set previous.next to previous.next.next
    # K is guaranteed to be < len(list)

    # Error case
    if not list:
        return []

    main = list
    referece = list
    for i in range(k + 1):
        referece = referece.next

    while referece is not None:
        main = main.next
        referece = referece.next
    
    main.next = main.next.next
    return list


ls = Node(1, Node(2, Node(3, Node(4, Node(5, None)))))
print(getList(ls))
# Remove the 4
print(getList(remove_kth_last(ls, 3)))

assert getList(remove_kth_last(Node(0, Node(3, Node(7, Node(8, Node(10, None))))), 2)) == [0, 3, 7, 10]
assert getList(remove_kth_last(Node(0, Node(3, Node(7, Node(8, Node(10, None))))), 4)) == [0, 7, 8, 10]
assert getList(remove_kth_last(Node(0, Node(3, Node(7, Node(8, Node(10, None))))), 1)) == [0, 3, 7, 8]