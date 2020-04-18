# Problem 14 - estiimate pi to nearest 3 decimals using monte carlo method
import random

def estimate():
    # 2x2 square with 1 radius
    radius = 0.5
    total = 0
    trials = 10000000

    # area of circle = pi * (0.5)^2 = pi/4
    # area of square = 1 * 1 = 1

    for _ in range(trials):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)

        if(pow(x, 2) + pow(y, 2) <= pow(radius, 2)):
            total += 1

    newTotal = 4 * (total/trials)
    print(round(newTotal, 3))

estimate()