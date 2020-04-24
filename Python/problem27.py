# Check if brackets are well formed

def checkBrackets(s):
    if s is None:
        return True

    stack = list()

    for i in range(len(s)):
        if s[i] == "{" or s[i] == "[" or s[i] == "(" or s[i] == "<":
            stack.append(s[i])
        else:
            # Check for empty list
            if len(stack) == 0:
                return False

            prev = stack.pop()
            if prev == "[" and s[i] == "]":
                continue
            elif prev == "(" and s[i] == ")":
                continue
            elif prev == "{" and s[i] == "}":
                continue
            elif prev == "<" and s[i] == ">":
                continue
            else:
                return False

    if len(stack) > 0:
        return False

    return True

assert checkBrackets("")
assert checkBrackets("{}")
assert checkBrackets("([])")
assert checkBrackets("([])[]({})")
assert not checkBrackets("(")
assert not checkBrackets("]")
assert not checkBrackets("((()")
assert not checkBrackets("([)]")