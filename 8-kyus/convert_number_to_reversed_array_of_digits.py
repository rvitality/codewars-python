# https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

# ! Convert number to reversed array of digits --------------


def digitize(n):
    return [int(num) for num in f"{n}"[::-1]]
