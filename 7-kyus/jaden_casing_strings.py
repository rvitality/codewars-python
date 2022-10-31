# https://www.codewars.com/kata/5390bac347d09b7da40006f6/train/python

# ! Jaden Casing Strings --------------


def to_jaden_case(string):
    return " ".join([word.capitalize() for word in string.split(" ")])
