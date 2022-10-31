# https://www.codewars.com/kata/5412509bd436bd33920011bc/train/python

# ! Credit Card Mask --------------


def maskify(cc):
    if len(cc) < 4:
        return cc
    length = len(cc) - 4
    return "#" * length + cc[length:]


print(maskify("4556364607935616"))
