threshold = 40

points = [[]]

# Read points
try:
    with open("points.txt", 'r') as f:
        for line in f:
            (x, y) = line.split(',')
            x, y = int(x), int(y)
            if x < threshold and y < threshold:
                points.append([])
            else:
                points[-1].append((x, y))
except FileNotFoundError as e:
    print("Put the file here")

# Separate hands
for i, clicks in enumerate(points):
    left, right = [], []
    finished_left = False
    for j, (x, y) in enumerate(clicks):
        if x > (400 - threshold) and y > (300 - threshold):
            finished_left = True
        else:
            if finished_left:
                right.append((x,y))
            else:
                left.append((x,y))
    if finished_left:
        points[i] = (left, right)
    else:
        points[i] = (left, )
