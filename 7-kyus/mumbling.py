# https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/python

# ! Mumbling --------------


def accum(s):
    return "-".join([(char * (index + 1)).title() for index, char in enumerate(s)])
