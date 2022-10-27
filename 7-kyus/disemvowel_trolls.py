# https://www.codewars.com/kata/52fba66badcd10859f00097e/train/python

# ! Disemvowel Trolls --------------


def disemvowel(string_):
    for vowel in "aeiouAEIOU":
        string_ = string_.replace(vowel, "")

    return string_
