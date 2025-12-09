import sys


points = []
for l in sys.stdin:
    points.append(list(map(int, l.strip().split(","))))
N = len(points)

max_area = 0

for i in range(N):
    for j in range(i+1, N):
        p1 = points[i]
        p2 = points[j]
        area = (1 + abs(p1[0] - p2[0])) * (1 + abs(p1[1] - p2[1]))

        if area > max_area: max_area = area

print(max_area)