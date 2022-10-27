# https://www.codewars.com/kata/54ff3102c1bad923760001f3/train/python

# ! Vowel Count --------------


def get_count(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    res = [char for char in sentence if char in vowels]
    return len(res)


get_count("Should count all vowels")
