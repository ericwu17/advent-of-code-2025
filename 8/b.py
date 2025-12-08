import sys

def dist(p1, p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)**0.5

ps = []
for l in sys.stdin:
    ps.append(list(map(int, l.strip().split(","))))
N = len(ps)

edges = []

for i in range(N):
    for j in range(i+1, N):
        edges.append(((i, j), dist(ps[i], ps[j])))

edges = list(reversed(sorted(edges, key = lambda e: e[1])))  # sort edges by length

print("edges sorted")

NN = 1000
crappy_union_find = [i for i in range(NN)]

def union(i, j):
    a = crappy_union_find[i]
    b = crappy_union_find[j]
    if a < b:
        for idx in range(NN):
            if crappy_union_find[idx] == b:
                crappy_union_find[idx] = a
    else:
        for idx in range(NN):
            if crappy_union_find[idx] == a:
                crappy_union_find[idx] = b
def is_same_circuit(i, j):
    return crappy_union_find[i] == crappy_union_find[j]


N_WIRES = int((N*(N-1))/2)
n_connections = 0
last_connected = (0, 1)
while True:
    print(n_connections)
    (i, j), weight = edges.pop()
    if is_same_circuit(i, j): 
        n_connections += 1
        if n_connections == N_WIRES:
            break
        continue

    union(i, j)
    n_connections += 1
    last_connected = (i, j)

    if n_connections == N_WIRES:
        break

i, j = last_connected
print(ps[i][0] * ps[j][0])

print("DONE")


