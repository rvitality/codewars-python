# https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python

# ! Remove the minimum --------------


def remove_smallest(numbers):
    if len(numbers) == 0:
        return []
    numbersCopy = numbers.copy()
    numbersCopy.remove(min(numbers))
    return numbersCopy


print(remove_smallest([5, 3, 2, 1, 4]))
