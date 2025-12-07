import sys

g = []

for l in sys.stdin:
    l = l.removesuffix('\n')
    g.append(list(l))

I = len(g)
J = len(g[0])

split_count = 0

def propagate(i, j):
    global split_count

    if g[i][j] == '^':
        propagate(i , j+1)
        propagate(i , j-1)
        split_count += 1
    elif g[i][j] == '|':
        return
    else:
        g[i][j] = '|'
        if i+1 < I:
            propagate(i+1, j)


for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == 'S':
            propagate(i+1, j)
            break


for i in range(len(g)):
    for j in range(len(g[i])):
        print(g[i][j], end = "")
    print("")
        




print(split_count)