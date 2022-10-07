#  https://www.codewars.com/kata/5769b3802ae6f8e4890009d2/train/python

# ! Removing Elements --------------

def remove_every_other(list):
    res = []
    for i in range(0, len(list), 2):
        res.append(list[i])

    return res

    #return list[::2]
    


















