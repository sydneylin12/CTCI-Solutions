# Find the palindrome that can be made by inserting the fewest number of characters

def nearestPalindrome(s):

    if not s:
        return ""
    
    # Case where no algorithm is needed
    elif isPalindrome(s):
        return s

    # Pointers to indexes
    front = s
    head = 0
    tail = len(s) - 1

    # Insert characters at the head of the string
    while head < tail:
        print("Head: " + front[head] + " Tail: " + front[tail])

        # If palindrome characters are equal
        if front[head] == front[tail]:
            head += 1
            tail -= 1
            continue
        else:
            print("Inserting: " + front[tail])
            front = front[:head] + front[tail] + front[head:]
            head += 1

    back = s
    head = 0
    tail = len(s) - 1

    # Insert characters at the tail end of the string
    while head < tail:
        if back[head] == back[tail]:
            head += 1
            tail -= 1
        else:
            print("Inserting at back: " + back[head])
            back = back[:tail + 1] + back[head] + back[tail + 1:]
            # Head and tail will automatically be equal and tail will be adjusted
            head += 1
    
    if len(front) == len(back):
        return min(front, back)
    elif len(front) < len(back):
        return front
    else:
        return back


def isPalindrome(s):
    if len(s) <= 1:
        return True
    if s[0] == s[len(s) - 1]:
        return isPalindrome(s[1:len(s) - 1])
    else:
        return False

assert nearestPalindrome("racecar") == "racecar"
assert nearestPalindrome("google") == "elgoogle"
assert nearestPalindrome("egoogle") == "elgoogle"
assert nearestPalindrome("elgoog") == "elgoogle"
assert nearestPalindrome("race") == "ecarace"