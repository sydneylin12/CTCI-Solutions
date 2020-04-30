# Problem 17
# Given a directory string, return the longest absolute path to a file

def longestAbsolutePath(dir):

    # Edge cases
    if not dir:
        return 0

    # File not found
    elif "." not in dir:
        return 0

    # Split across the new line
    arr = dir.split("\n")

    # Count current number of tabs
    tabs = arr[0].count("\t")

    # Return string starting with first element
    length = 0
    first = arr[0].replace("\t", "")

    # Iterate through the directory (EXCLUDING FIRST ELEMENT)
    print(arr)

    if len(arr) == 1 and "." in arr[0]:
        temp = arr[0].replace("\t", "")
        return len(temp)

    for directory in arr[1:]:

        # If there is a child directory (1 more tab)
        if directory.count("\t") == tabs + 1:

            # Find index of substring/subdirectory in the original string
            idx = dir.find(directory)

            # Recursively call on the substring
            result = len(first) + longestAbsolutePath(dir[idx:])
            if(result > length):
                length = result

        # Reached a directory above
        elif directory.count("\t") == tabs:
            break

    return length

assert longestAbsolutePath("dir\n\tsubdir1\n\tsubdir2") == 0
assert longestAbsolutePath("dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext") == 18
assert longestAbsolutePath("dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext") == 29