# The bouncing ball
height = 100 #height in meters
bounce = 1
while bounce < 11:
    height = height * 0.6
    print(bounce, ":", end = ' ')
    print(round(height, 4))
    bounce = bounce + 1
