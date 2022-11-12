# https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

# ! Count of positives / sum of negatives --------------


def count_positives_sum_negatives(arr):
    if len(arr) == 0:
        return []
    count_of_positives = 0
    sum_of_negatives = 0
    for num in arr:
        if num < 0:
            sum_of_negatives += num

        if num > 0:
            count_of_positives += 1

    return [count_of_positives, sum_of_negatives]
