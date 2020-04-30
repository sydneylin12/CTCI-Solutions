# Problem 14 - estiimate pi to nearest 3 decimals using monte carlo method
import random

def estimate():
    # 2x2 square with 1 radius
    radius = 2
    total = 0
    trials = 100000000

    newRad = pow(radius, 2)

    for _ in range(trials):
        x = random.uniform(-radius, radius)
        y = random.uniform(-radius, radius)

        if pow(x, 2) + pow(y, 2) < newRad:
            total += 1

    return 4 * (total/trials)

