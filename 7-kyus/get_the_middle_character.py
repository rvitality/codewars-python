# https://www.codewars.com/kata/56747fd5cb988479af000028/train/python

# ! Get the Middle Character --------------
import math


def get_middle(s):
    str_len = len(s)
    mid = str_len / 2
    if str_len % 2 == 0:
        return s[int(mid - 1) : int(mid + 1)]
    return s[math.floor(mid)]


print(get_middle("middle"))
