# https://www.codewars.com/kata/566fc12495810954b1000030/train/python

# ! Count the Digit --------------


def nb_dig(n, d):
    count = 0
    for num in range(0, n + 1):
        str_d = f"{d}"
        str_num_squared = f"{num**2}"
        if str_d in str_num_squared:
            count += str_num_squared.count(str_d)

    return count


nb_dig(12224, 8)
