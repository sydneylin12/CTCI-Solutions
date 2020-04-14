import time

# Daily coding problem 10 - scheduler
# Call a funciton f after n milliseconds
def schedule(f, n):
    # Sleep for n milliseconds
    time.sleep(n / 1000)
    return f()

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def foo():
    print("Called from foo!")

def main():
    schedule(foo, 3000)

if __name__ == "__main__":
    main()