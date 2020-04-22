# Probelm 22
# Sentence to list of words

def sentenceToList(s, dict):
    current = ""
    ret = []

    for i in s:
        current += i
        if current in dict:
            ret.append(current)
            current = ""
    return ret

s = "thequickbrownfox"
dict = ["quick", "brown", "fox", "the"]
print(sentenceToList(s, dict))

s = "bedbathandbeyond"
dict = ["bed", "bath", "bedbath", "and", "beyond"]
print(sentenceToList(s, dict))