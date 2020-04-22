# Problem 23
# robot in grid probelm
import sys

# solution = 7
mat = \
    [["f", "f", "f", "f"], 
    ["t", "t", "f", "t"], 
    ["f", "f", "f", "f"], 
    ["f", "f", "f", "f"]]

start = (3, 0)
end = (0, 0)

# Find the shortest path given a start node, end node, and matrix
def shortestPath(start, end, mat, visited):

    i = start[0]
    j = start[1]
    visited.append((i, j))
    original = visited.copy()

    # Bad path because of t node
    if mat[i][j] == "t":
        return sys.maxsize

    # Got to the end
    if i == end[0] and j == end[1]:
        return 0

    up = sys.maxsize
    down = sys.maxsize
    left = sys.maxsize
    right = sys.maxsize

    # Down
    if i + 1 < len(mat) and (i + 1, j) not in visited:
        print("Down")
        newStart = (i + 1, j)
        down = 1 + shortestPath(newStart, end, mat, visited)
        visited = original.copy()

    # Up
    if i - 1 >= 0 and (i - 1, j) not in visited:
        print("Up")
        newStart = (i - 1, j)
        up = 1 + shortestPath(newStart, end, mat, visited)
        visited = original.copy()

    # Right
    if j + 1 < len(mat[0]) and (i, j + 1) not in visited:
        print("Left")
        newStart = (i, j + 1)
        right = 1 + shortestPath(newStart, end, mat, visited) 
        visited = original.copy()

    # Left
    if j - 1 >= 0 and (i, j - 1) not in visited:
        print("Right")
        newStart = (i, j - 1)
        left = 1 + shortestPath(newStart, end, mat, visited) 
        visited = original.copy()

    return min(up, down, left, right)

print(shortestPath(start, end, mat, []))
