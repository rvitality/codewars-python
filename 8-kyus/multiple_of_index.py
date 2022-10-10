# https://www.codewars.com/kata/5a34b80155519e1a00000009/train/python

# ! Multiple of index --------------


def multiple_of_index(arr):
    return [arr[i] for i in range(1, len(arr)) if arr[i] % i == 0]


# result =
