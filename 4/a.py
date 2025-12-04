import sys

g = []

for l in sys.stdin:
    g.append(list(l.strip()))

N = len(g)

g = [['.'] * N] + g + [['.'] * N]

g = [['.'] + l + ['.'] for l in g]


n_removed = 0
while True:
    removed_this_iter = False
    for i in range(len(g)):
        for j in range(len(g[i])):
            if g[i][j] == '@':
                n_adj = 0
                for di in (-1, 0, 1):
                    for dj in (-1, 0, 1):
                        if di == 0 and dj == 0:
                            continue
                        if g[i+di][j+dj] == '@':
                            n_adj += 1
                if n_adj < 4:
                    n_removed += 1
                    removed_this_iter = True
                    g[i][j] = '.'
    if not removed_this_iter:
        break



print(n_removed)