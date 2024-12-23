import random


def gen_random(count, minValue, maxValue):
    a = [random.randint(minValue, maxValue) for i in range(count)]
    return a

#print(gen_random(5, 1, 3))