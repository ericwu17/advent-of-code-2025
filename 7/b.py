import sys

g = []

for l in sys.stdin:
    l = l.removesuffix('\n')
    g.append(list(l))

I = len(g)
J = len(g[0])

path_count = 0

cache = {}

def get_path_count(i, j):
    global path_count

    if (i, j) in cache.keys():
        return cache[(i,j)]


    if g[i][j] == '^':
        cache[(i,j)] = get_path_count(i, j+1) + get_path_count(i, j-1)
        return cache[(i,j)]
    else:
        g[i][j] = '|'
        if i+1 < I:
            cache[(i,j)] = get_path_count(i+1, j)
            return cache[(i,j)]
        else:
            cache[(i,j)] = 1
            return 1


for i in range(len(g)):
    for j in range(len(g[i])):
        if g[i][j] == 'S':
            print(get_path_count(i+1, j))
            break


# for i in range(len(g)):
#     for j in range(len(g[i])):
#         print(g[i][j], end = "")
#     print("")
        




# print(path_count)