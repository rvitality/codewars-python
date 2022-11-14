# https://www.codewars.com/kata/55d1d6d5955ec6365400006d/train/python

# ! Round up to the next multiple of 5 --------------


def round_to_next5(n):
    if n == 0 or n % 5 == 0:
        return n
    diff = n % 5
    return n + 5 - diff
