# DCP problem 5
# This took me way longer that it should have

def cons(a, b):
    def pair(f): 
        # Calls a function with two parameters
        return f(a, b)
    return pair

def car(pair):
    # Inner function for "unpacking" first element
    def temp(a, b):
        return a
    # Explanation: cons returns a function, called pair
    # Pair is what is passed in
    # Pair has one parameter, f, which is a function
    # Pair calls the function f
    # Our inner function (called in f's place) returns the first element
    # Temp has two parameters, a and b, and it is able to access the data in the cons
    # The temp function returns the first element of a and b, so calling this will return the car
    return pair(temp)

def cdr(pair):
    # Inner function for "unpacking" second element
    def temp(a, b):
        return b
    return pair(temp)

assert car(cons(3, 4)) == 3
assert cdr(cons(3, 4)) == 4