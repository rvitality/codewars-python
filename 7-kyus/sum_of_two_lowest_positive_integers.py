# https://www.codewars.com/kata/558fc85d8fd1938afb000014/train/python

# ! Sum of two lowest positive integers --------------


def sum_two_smallest_numbers(numbers):
    smallest1 = None
    smallest2 = None

    for num in numbers:
        if not smallest1 or num < smallest1:
            smallest2 = smallest1
            smallest1 = num
        elif not smallest2 or num < smallest2:
            smallest2 = num

    return smallest1 + smallest2
    # sorted_numbers_asc = sorted(numbers)
    # return sorted_numbers_asc[0] + sorted_numbers_asc[1]
