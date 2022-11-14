# https://www.codewars.com/kata/583f158ea20cfcbeb400000a/train/python

# ! Make a function that does arithmetic! --------------


def arithmetic(a, b, operator):
    operations = {
        "add": a + b,
        "subtract": a - b,
        "multiply": a * b,
        "divide": a / b,
    }

    return operations[operator]
