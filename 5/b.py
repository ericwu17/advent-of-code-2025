import sys

ranges = []

while True:
    l = input().strip()
    if l == "": break
    a, b  = l.split("-")
    ranges.append([int(a), int(b)])


ranges = sorted(ranges, key = lambda r: r[0])
merged_ranges = [ranges[0]]
for r in ranges[1:]:
    if r[0] <= merged_ranges[-1][1]:
        # merge the two intervals
        merged_ranges[-1][1] = max(merged_ranges[-1][1], r[1])
    else:
        merged_ranges.append(r)

print(merged_ranges)

count = sum([r[1] - r[0] + 1 for r in merged_ranges])

print(count)

