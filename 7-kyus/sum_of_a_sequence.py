# https://www.codewars.com/kata/586f6741c66d18c22800010a/train/python

# ! Sum of a sequence --------------


def sequence_sum(begin_number, end_number, step):
    return sum([num for num in range(begin_number, end_number + 1, step)])
