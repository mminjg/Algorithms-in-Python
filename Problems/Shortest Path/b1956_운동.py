import sys
input = sys.stdin.readline
INF = int(1e9)

v, e = map(int, input().split())
graph =[[INF] * (v + 1) for _ in range(v + 1)]

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a][b] = c

for k in range(1, v + 1):
    for a in range(1, v + 1):
        for b in range(1, v + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

min_value = INF
for a in range(v + 1):
    for b in range(v + 1):
        if a == b and graph[a][b] != INF:
            min_value = min(min_value, graph[a][b])

if min_value == INF:
    print(-1)
else:
    print(min_value)