# Problem 19
# Given an NxK matrix where [n][k] = cost to build nth house with kth color, return minimum cost
import sys

def minCost(mat):
    indexes = []
    colors = []
    n = len(mat)
    k = len(mat[0])

    # Reverse the matrix
    for i in range(n):

        # Minimum cost set to largest possible value (INT.MAX)
        min = sys.maxsize
        idx = -1 # Color set to none (-1)

        for j in range(k):

            # If the color is less than the minimum
            if mat[i][j] < min:

                # If we can choose any min value for first house
                if len(indexes) == 0:
                    min = mat[i][j]
                    idx = j

                # Color of the house is not adjacent
                elif indexes[len(indexes) - 1] != j:
                    min = mat[i][j]
                    idx = j

                # Color of the house is adjacent
                else:
                    continue

        indexes.append(idx)
        colors.append(min)

    return sum(colors)


# 4 = n, 6 = k
mat = \
    [[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6],
     [10, 1, 4, 9, 7, 6]]

# Solution: 8
print(minCost(mat))