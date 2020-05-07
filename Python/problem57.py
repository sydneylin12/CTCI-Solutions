# Break a string into multiple texts so each as length k or less
# Words cannot break across lines

def breakText(s, k):
    arr = s.split(" ")
    
    current = ""
    n = []

    for i in arr:
        if len(current) + len(i) > k:
            n.append(current)
            current = i
        elif current == "":
            current += i
        else:
            current += " " + i

    if len(current) > k:
        return None

    n.append(current)
    return n



assert not breakText("encyclopedia", 8)
assert breakText("the quick brown fox jumps over the lazy dog", 10) == [
    "the quick", "brown fox", "jumps over", "the lazy", "dog"]