# String run length encoding

def encode(s):
    if not s:
        return ""

    curr = s[0]
    count = 0
    ret = ""

    for i in s:
        print
        if i == curr:
            count += 1
        else:
            ret += str(count) + curr
            curr = i
            count = 1

    # Extra characters
    ret += str(count) + curr
    return ret

# Assume the string is PROPERLY encoded
def decode(s):
    if not s:
        return ""

    ret = ""
    for i in range(len(s)):
        count = 0
        if s[i].isnumeric():
            count = int(s[i])
            next = s[i+1]
            for i in range(count):
                ret += next
    return ret

assert encode("") == ""
assert encode("AAA") == "3A"
assert encode("AAAABBBCCDAA") == "4A3B2C1D2A"

assert decode("") == ""
assert decode("3A") == "AAA"
assert decode("4A3B2C1D2A") == "AAAABBBCCDAA"