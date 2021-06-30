import sys
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b

p, w = map(int, input().split())
c, v = map(int, input().split())

edges = []
parent = [0] * p
for i in range(p):
    parent[i] = i

for _ in range(w):
    s, e, width = map(int, input().split())
    edges.append((width, s, e))

edges.sort(reverse=True)

min_width = edges[0][0]
for edge in edges:
    width, a, b = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        if find_parent(parent, c) == find_parent(parent, v):
            min_width = width
            break

print(min_width)