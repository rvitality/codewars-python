# https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python

# ! Exes and Ohs --------------


def is_isogram(s):
    for index in range(0, len(s)):
        char = s[index].lower()
        if index != s.lower().find(char):
            return False
    return True


# pythonic way
# return len(string) == len(set(string.lower()))
