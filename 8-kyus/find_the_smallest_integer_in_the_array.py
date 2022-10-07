# https://www.codewars.com/kata/55a2d7ebe362935a210000b2/train/python

# ! Find the smallest integer in the array --------------

def find_smallest_int(arr):
    min = arr[0]

    for i in arr:
        print(min, i) 
        if(i < min):
            min = i

    return min


    # pythonic way
    # return min(arr)







