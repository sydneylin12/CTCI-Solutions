# Problem 12 - number of steps

# Count the number of ways a staircase with N steps could be climbed
# Bonus: Use a set for the number of ways to climb
def steps(n, ways):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        temp = 0
        for i in ways:
            temp += steps(n - i, ways)
        return temp

assert steps(4, [1, 2]) == 5
assert steps(4, [1, 2, 3]) == 7
