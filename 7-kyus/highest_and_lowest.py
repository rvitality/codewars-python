# https://www.codewars.com/kata/554b4ac871d6813a03000035/train/python

# ! Highest and Lowest --------------


def high_and_low(numbers):
    numbers_list = [int(num) for num in numbers.split(" ")]
    return f"{max(numbers_list)} {min(numbers_list)}"
