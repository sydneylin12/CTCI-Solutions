# Edit distance between 2 strings

def editDistance(a, b):

    ops = 0

    # Can be solved by substituting
    if len(a) == len(b):
        for i in range(len(a)):
            if a[i] != b[i]:
                ops += 1
        return ops

    else:

        # This makes the algorithm run in O(n^2)
        while len(a) != len(b):
            # Insertion
            if len(a) < len(b):
                if matchingCharacters(b[0] + a, b) > matchingCharacters(a + b[len(b) - 1], b):
                    a = b[0] + a
                else:
                    a = a + b[len(b) - 1]

            # Deletion
            else:
                if matchingCharacters(a[1:], b) > matchingCharacters(a[:len(a) - 1], b):
                    a = a[1:]
                else:
                    a = a[:len(a) - 1]

            ops += 1
            
        # Clean up with replacement
        for i in range(len(a)):
            if a[i] != b[i]:
                ops += 1
        return ops


def matchingCharacters(a, b):
    matches = 0
    for i in range(min(len(a), len(b))):
        if a[i] == b[i]:
            matches += 1
    return matches

def editDistanceRecursive(s1, s2):
    if s1 == s2:
        return 0
    elif not s1:
        return len(s2)
    elif not s2:
        return len(s1)
    else:
        if s1[0] == s2[0]:
            return editDistanceRecursive(s1[1:], s2[1:])
        return 1 + min(
            editDistanceRecursive(s1[1:], s2), # Deletion
            editDistanceRecursive(s1, s2[1:]), # Addition
            editDistanceRecursive(s1[1:], s2[1:]) # Replacement
        )


assert editDistance("", "") == 0
assert editDistance("a", "b") == 1
assert editDistance("abc", "") == 3
assert editDistance("abc", "abc") == 0
assert editDistance("kitten", "sitting") == 3

assert editDistanceRecursive("", "") == 0
assert editDistanceRecursive("a", "b") == 1
assert editDistanceRecursive("abc", "") == 3
assert editDistanceRecursive("abc", "abc") == 0
assert editDistanceRecursive("kitten", "sitting") == 3