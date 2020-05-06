# Implement a URL shortener
import random

class UrlShortener:
    def __init__(self):
        self.dict = dict()
        self.letters = dict()

        for i in range(26):
            self.letters[chr(97 + i)] = 1
        print(self.letters)

    def shorten(self, url):
        segments = len(url) // 6 + 1
        short = ""

        for _ in range(6):

            # Get random character from dictionary
            c = chr(random.randint(0, 25) + 97)
            count = self.letters[c]

            while count == 0:
                c = chr(random.randint(0, 25) + 97)
                count = self.letters[c]

            if len(url) > segments:
                self.dict[c] = url[:segments]
                url = url[segments:]
                
            else:
                self.dict[c] = url

            self.letters[c] -= 1
            short += c

        print(short)
        print(self.dict)
        return short

    def restore(self, short):

        ret = ""
        for i in range(len(short)):
            ret += self.dict[short[i]]

        print(ret)
        return ret


url_0 = "https://www.tutorialspoint.com/python/string_replace.htm"
us = UrlShortener()
short_0 = us.shorten(url_0)
assert us.restore(short_0) == url_0
short_1 = us.shorten(url_0)
assert us.restore(short_1) == url_0