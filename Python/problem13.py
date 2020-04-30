# Problem 13
# Given an int k and string s: 
# Find the longest substring that contains at most k distinct characters
# My solution - O(n^2) time and O(1) space

def findSubstring(str, k):

    # Initialize variables
    subs = []

    # Keep track of the character counts
    map = {}

    # Current string
    current = ""

    # Iterate through the string nested - O(n^2)
    for i in range(len(str)):
        for j in range(i, len(str)):

            # If the current character would cause the map to exceed k characters
            if(len(map) == k and str[j] not in map):
                # Reset all values and append current string
                subs.append(current)
                current = ""
                map.clear()
                break
            else:
                # Add on current character and set to found in the map
                current += str[j]
                map[str[j]] = 1
    
    # If the entire thing is acceptable
    if not subs:
        return str

    current = ""
    # Find the longest one in the set of substrings with k characters
    for substring in subs:
        if(len(substring) > len(current)):
            current = substring
    return current

assert findSubstring("abcba", 2) == "bcb"
assert findSubstring("abccbba", 2) == "bccbb"
assert findSubstring("abcbbbabbcbbadd", 2) == "bbbabb"
assert findSubstring("abcbbbaaaaaaaaaabbcbbadd", 1) == "aaaaaaaaaa"
assert findSubstring("abccbba", 3) == "abccbba"