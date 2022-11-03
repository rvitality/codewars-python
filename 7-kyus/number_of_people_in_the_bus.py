# https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

# ! Number of People in the Bus --------------


def number(bus_stops):
    still_in = 0
    for (got_in, dropped) in bus_stops:
        still_in += got_in - dropped
    return still_in

    # return sum([stop[0] - stop[1] for stop in bus_stops])
