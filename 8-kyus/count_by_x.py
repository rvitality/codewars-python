# https://www.codewars.com/kata/5513795bd3fafb56c200049e/train/python

# ! Count by X --------------
def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    return [num for num in range(x, x * n + 1, x)]
