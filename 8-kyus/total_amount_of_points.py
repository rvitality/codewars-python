#  https://www.codewars.com/kata/5bb904724c47249b10000131/train/python

# ! Total amount of points --------------

def points(games):
    total_points = 0
    
    for score in games:
        [x, y] = score.split(":")

        # x = int(x)
        # y = int(y)

        if(x > y):
            total_points += 3
        elif(x == y):
            total_points += 1

    return total_points
    
