# Problem 7 - find decoding of strings
# Pass in a string with numbers
def decode(s):
    s = str(s)
    if s == "" or len(s) == 0:
        return 1

    first = s[0:1]
    firstSum = 0
    secondSum = 0
    if int(first) > 0 and int(first) < 10:
        firstSum += decode(s[1:])

    if len(s) > 1:
        second = s[0:2]
        if int(second) > 9 and int(second) < 27:
            secondSum += decode(s[2:])
    
    return firstSum + secondSum

assert decode(81) == 1
assert decode(11) == 2
assert decode(111) == 3
assert decode(1111) == 5
assert decode(1311) == 4
