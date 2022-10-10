# https://www.codewars.com/kata/5dd462a573ee6d0014ce715b/train/python

# ! Check same case --------------


def same_case(a, b):
    return a.isupper() == b.isupper() if a.isalpha() and b.isalpha() else -1
