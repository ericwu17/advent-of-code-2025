import sys

ranges = []

while True:
    l = input().strip()
    if l == "": break
    a, b  = l.split("-")
    ranges.append((int(a), int(b)))

count = 0;

for l in sys.stdin:
    i  = int(l.strip())
    is_fresh = False
    for r in ranges:
        if i >= r[0] and i <= r[1]:
            is_fresh = True
            break
    if is_fresh:
        count += 1

print(count)