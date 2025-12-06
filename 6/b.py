import sys

def product_(ns):
    res = 1
    for n in ns:
        res = res * n
    return res


lines_transposed = []
for l in sys.stdin:
    l = l.removesuffix('\n')
    lines_transposed.append(l)

lines = ["".join([line[i] for line in lines_transposed]) for i in range(len(lines_transposed[0]))]

i = 0 
gt = 0
while i < len(lines):
    l = lines[i].strip()
    op = l[-1]
    nums = [int(l[:-1])]
    i += 1

    while  i < len(lines):
        l = lines[i].strip()
        if l == "": 
            i += 1
            break
        nums.append(int(l))
        i += 1

    if op == '+':
        gt += sum(nums)
    else:
        gt += product_(nums)

print(gt)