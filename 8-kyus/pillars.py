#  https://www.codewars.com/kata/5bb0c58f484fcd170700063d/train/python

# ! Pillars --------------


def pillars(num_pill, dist, width):
    if(num_pill < 2): return 0

    # convert to cm
    dist_cm = dist * 100;

    # add width to a single pillar
    pillar_width_and_distance = dist_cm + width

    # how wide all the pillars are from 1st to last
    pillars_total_width = num_pill * pillar_width_and_distance 

    # subtract the width of first and last pillar
    pillars_total_width = pillars_total_width - (width * 2)

    # if pillars are 3, there are only 2 distances in between
    # the distances between pillars is 1 less than the number of pillars
    pillars_total_width = pillars_total_width - dist_cm 

    return pillars_total_width





