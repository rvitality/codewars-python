# https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/python

# ! List Filtering --------------


def filter_list(l):
    "return a new list with the strings filtered out"
    return [num for num in l if type(num) == int]


print(type(5))
