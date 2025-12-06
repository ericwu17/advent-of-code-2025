
import sys

nums = []
for l in sys.stdin:
    l = l.strip()
    if l[0].isdigit():
        nums.append(list(map(int, l.strip().split())))
    else:
        ops= list(l.strip().split())

print(nums)
print(ops)


def product_(ns):
    res = 1
    for n in ns:
        res = res * n
    return res

count = 0
for i in range(len(ops)):
    op = ops[i]
    ns = [n[i] for n in nums]
    if op == '+':
        count += sum(ns)
    else:
        count += product_(ns)

print(count)