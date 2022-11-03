# https://www.codewars.com/kata/5259b20d6021e9e14c0010d4/train/python

# ! Reverse words --------------


def reverse_words(text):
    return " ".join([word[::-1] for word in text.split(" ")])


print(reverse_words("The quick brown fox jumps over the lazy dog."))
