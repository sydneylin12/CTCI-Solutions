# Daily coding problem 11 - query string

# Return a list of autocompleted queries
# O(n) time and O(n) space
def query(s, queries):
    ret = []
    for query in queries:
        # Check for length first and then check for the first substring of the query word
        if len(query) >= len(s) and query[0: len(s)] == s:
            ret.append(query)
    return ret

s = "de"
queries = ["dog", "deer", "deal", "dead", "dank"]
print(query(s, queries))