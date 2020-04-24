# Justify text to line length K

def justify(strings, k):

    if not strings:
        return []

    temp = []
    current = []
    currentStr = ""

    # Iterate through the array
    for i in strings:

        # If length exceeds, reset and add to temporary array
        if len(currentStr) + len(i) > k:
            temp.append(currentStr)
            currentStr = ""
            current.clear()

        # Must be another if to include all characters
        if len(currentStr) + len(i) < k:
            current.append(i)
            currentStr = " ".join(current)

    # Handle any left over strings
    temp.append(currentStr)

    # Return array
    ret = []

    # Iterate through the result array
    for i in temp:
        # If length is OK
        if len(i) == k:
            continue
        else:
            # Count number of spaces needed
            needed = k - len(i)            
            idx = 0

            # Distribute the spaces across the letters
            while needed > 0:
                if i[idx] == " ":
                    i = i[:idx] + " " + i[idx:]
                    needed -= 1

                    # Advance to the next non whitespace character
                    while i[idx] == " ":
                        idx += 1

                # Increment index after conditional
                idx += 1

                # Make sure indexes do not go OOB
                if idx == len(i):
                    idx = 0
                
            ret.append(i)

    return ret

justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16)               
assert justify(["the", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog"], 16) == ['the  quick brown', 'fox  jumps  over', 'the   lazy   dog']
assert justify(["the", "quick", "brown", "fox", "jumps", "over"], 16) == ['the  quick brown', 'fox  jumps  over']
assert justify(["the", "quick"], 16) == ['the        quick']