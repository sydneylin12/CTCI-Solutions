# Problem 17
# Given a directory string, return the longest absolute path to a file

x = "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

def longestAbsolutePath(dir):
    # Split across the new line
    arr = dir.split("\n")
    #print(arr)

    # Check for empty array
    if len(arr) == 0:
        return ""

    # Return the file if found (.ext)
    elif ".ext" in arr[0]:
        return arr[0]

    # Empty subdirectory
    elif "." not in arr[0] and len(arr) == 1:
        return ""

    # Count current number of tabs
    tabs = arr[0].count("\t")

    # Return string starting with first element
    longest = ""
    first = arr[0]

    # Iterate through the directory (EXCLUDING FIRST ELEMENT)
    for directory in arr[1::]:

        # If there is a child directory (1 more tab)
        if directory.count("\t") == tabs + 1:
            print("Child found!: " + str(directory))
            # Find index of substring/subdirectory
            idx = x.find(directory)
            # Recursively call on the substring
            result = first + longestAbsolutePath(x[idx::])
            if(len(result) > len(longest)):
                longest = result

        # Reached a directory above
        elif directory.count("\t") == tabs:
            break
            
    return longest

result = "/".join(longestAbsolutePath(x).split())
print(len(result))
print(result)