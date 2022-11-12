# https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/python

# ! Basic Mathematical Operations --------------


def basic_op(operator, value1, value2):
    operations = {
        "+": value1 + value2,
        "-": value1 - value2,
        "*": value1 * value2,
        "/": value1 / value2,
    }

    return operations[operator]
