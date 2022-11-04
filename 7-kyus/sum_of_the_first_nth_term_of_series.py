# https://www.codewars.com/kata/555eded1ad94b00403000071/train/python

# ! Sum of the first nth term of Series --------------


def series_sum(n):
    divisor = 1
    sum = 0
    for index in range(n):
        sum += 1 / divisor

        divisor += 3

    return format(round(sum, 2), ".2f")


print(series_sum(10))
print(series_sum(5))
print(series_sum(1))
