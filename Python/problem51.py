# Given a function that generates perfectly random numbers between 1 and k inclusive, write a function that shuffles a deck of cards
# Represented with an array of only swaps
import random

def shuffle(deck):
    for i in range(len(deck)):
        j = random.randint(0, 51)
        swap(deck, i, j)
    return deck

def swap(a, i, j):
    temp = a[i]
    a[i] = a[j]
    a[j] = temp


cards = [x for x in range(52)]

for _ in range(10):
    assert all(x in shuffle(cards) for x in range(52))