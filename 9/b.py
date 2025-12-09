import sys
import matplotlib.pyplot as plt
# Note: 429731904 TOO LOW

points = []
for l in sys.stdin:
    points.append(list(map(int, l.strip().split(","))))
N = len(points)



max_x = max(p[0] for p in points)
max_y = max(p[1] for p in points)
min_x = min(p[0] for p in points)
min_y = min(p[1] for p in points)
xs = [p[0] for p in points]
ys = [p[1] for p in points]

# print(max_x, max_y, min_x, min_y)
# print(len(xs))
# print(len(ys))

# plt.scatter(xs, ys)
for i in range(N-1):
    x1, y1 = points[i]
    x2, y2 = points[i+1]
    plt.plot([x1, x2], [y1, y2], color = "#FF0000")
plt.show()

# after plotting the points, it looks like a big circle, with a massive slit cut out horizontally in the middle
# therefore I think the biggest rectangle would happen horizontally... with one of the points being the points on the slit.

SLIT_LOWER_X = 94582
SLIT_LOWER_Y = 48356
SLIT_UPPER_X = 94582
SLIT_UPPER_Y = 50408
SLIT_IDX_LOWER = 249
SLIT_IDX_UPPER = 248

MAX_Y = 68094   # maximum value of Y to be considered for a candidate point on top half
MIN_Y = 32527


# upper half first
upper_max_area = 0
i = 124
while points[i][1] > MAX_Y: 
    i += 1
print("start index for top half is ", i)

while i < SLIT_IDX_UPPER:
    px, py = points[i]
    point_ok = True
    for j in range(1, 20):
        i_ = i + j
        if i_ >= SLIT_IDX_UPPER: break
        
        if points[i_][0] > px:
            point_ok = False

    if point_ok:
        area = (1 + abs(px - SLIT_UPPER_X)) * (1 + abs(py - SLIT_UPPER_Y))
        if area > upper_max_area: upper_max_area = area
    
    i += 1

print("upper max area is ", upper_max_area)

# lower half next!
lower_max_area = 0
i = 372
while points[i][1] < MIN_Y: 
    i -= 1
print("start index for bottom half is ", i)

while i > SLIT_IDX_LOWER:
    px, py = points[i]
    point_ok = True
    for j in range(1, 20):
        i_ = i - j
        if i_ <= SLIT_IDX_LOWER: break
        
        if points[i_][0] > px:
            point_ok = False
    if point_ok:
        area = (1 + abs(px - SLIT_LOWER_X)) * (1 + abs(py - SLIT_LOWER_Y))
        if area > lower_max_area: lower_max_area = area
    i -= 1
print("lower max area is ", lower_max_area)
