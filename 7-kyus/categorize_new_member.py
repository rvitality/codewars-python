# https://www.codewars.com/kata/5502c9e7b3216ec63c0001aa/train/python

# ! Categorize New Member --------------


def open_or_senior(data):
    # res = []
    # for age, handicap in data:
    #     if age >= 55 and handicap > 7:
    #         res.append("Senior")
    #     else:
    #         res.append("Open")
    # return res
    return [
        "Senior" if age >= 55 and handicap > 7 else "Open" for (age, handicap) in data
    ]
