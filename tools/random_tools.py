import random


def random_string(item,length):
    res = random.choices(item,k = length)
    return "".join(res)