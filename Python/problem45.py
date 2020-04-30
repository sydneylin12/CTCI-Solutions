# Using a function that returns an integer from 1 to 5 (inclusive) with uniform probability, implement rand7
# Not sure how to do this one

import random

def rand5():
    return random.randint(1, 5)

def rand7():
    i = 5 * rand5() + rand5() - 5
    if i < 22:
        return i % 7 + 1
    return rand7()

num_experiments = 100000
result_dict = dict()
for _ in range(num_experiments):
    number = rand7()
    if number not in result_dict:
        result_dict[number] = 0
    result_dict[number] += 1

desired_probability = 1 / 7
for number in result_dict:
    result_dict[number] = result_dict[number] / num_experiments
    print(result_dict)
    assert round(desired_probability, 2) == round(result_dict[number], 2)