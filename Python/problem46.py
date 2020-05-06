# Longest palindromic substring

# MY SOLUTION DOES NOT WORK FOR ALL CASES
def longestPalindromicSubstring(s):
    start = 0
    end = len(s)

    substrings = []
    maxLen = 0

    # O(n)
    while start < end:
        current = s[start]
        last = s.rindex(current)
        substrings.append(s[start:last + 1])
        start += 1

    substrings.sort(key = len)
    substrings.reverse()
    
    for i in substrings:
        if isPalindrome(i):
            return i

    return None

# Helper method
def isPalindrome(s):
    return s == s[::-1]

def recursiveSolution(s):
    if not s:
        return None
    elif isPalindrome(s):
        return s
    
    sliceFirst = s[1:]
    sliceLast = s[:-1]

    rec1 = recursiveSolution(sliceFirst)
    rec2 = recursiveSolution(sliceLast)
    
    if len(rec1) > len(rec2):
        return rec1
    else:
        return rec2


assert recursiveSolution("aabcdcb") == "bcdcb"
assert recursiveSolution("bananas") == "anana"