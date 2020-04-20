# Problem 19
# Given an NxK matrix where [n][k] = cost to build nth house with kth color, return minimum cost
import sys

def minCost(mat):
    indexes = []
    # Reverse the matrix
    for i in range(len(mat[0])): # 6
        min = sys.maxsize
        color = -1
        for j in range(len(mat)): # 4
            if mat[j][i] < min:

                # If we can choose any min value
                if len(indexes) == 0:
                    min = mat[j][i]
                    color = j

                # Color of the house is not adjacent
                elif indexes[len(indexes) - 1] != j:
                    min = mat[j][i]
                    color = j

                # Color of the house is adjacent
                else:
                    continue

        indexes.append(color)

    result = 0
    for i in range(len(indexes)):
        result += mat[indexes[i]][i]

    return result


# 6 houses, 4 colors
mat = \
    [[7, 3, 8, 6, 1, 2],
     [5, 6, 7, 2, 4, 3],
     [10, 1, 4, 9, 7, 6],
     [10, 1, 4, 9, 7, 6]]

# Solution: 5, 1, 4, 2, 1, 3

print(minCost(mat))