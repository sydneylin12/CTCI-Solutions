# Problem 21
# Find minimum amount of rooms for overlapping classes
# Not sure if this is right

def rooms(arr):

    if not arr:
        return 0

    startDict = dict()
    endDict = dict()

    # Add start and end times to two dictionaries
    for start, end in arr:
        if start not in startDict:
            startDict[start] = 1
        else:
            startDict[start] += 1

        if end not in endDict:
            endDict[end] = 1
        else:
            endDict[end] += 1

    # Get min and max time interval
    earliest = min(startDict.keys())
    latest = max(endDict.keys())
    
    # Maximum number of classrooms
    maxClassCount = 0

    # Number of classrooms to fill current interval
    currentClassCount = 0

    # Iterate through the interval
    # Dictionary keys are times, values are counts
    for i in range(earliest, latest):

        # If the start time is in the dictionary
        if i in startDict:
            currentClassCount += startDict[i]

            # If another classroom is needed/if current classroom count exceeds max
            if currentClassCount > maxClassCount:
                maxClassCount = currentClassCount

        # If the end time is in the dictionary
        if i in endDict:
            currentClassCount -= endDict[i]

    return maxClassCount

# Copied test cases from github
assert rooms([]) == 0
assert rooms([(30, 75), (0, 50), (60, 150)]) == 2
assert rooms([(30, 75), (0, 50), (10, 60), (60, 150)]) == 3
assert rooms([(60, 150)]) == 1
assert rooms([(60, 150), (150, 170)]) == 2
assert rooms([(60, 150), (60, 150), (150, 170)]) == 3