import sys
from collections import deque
input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)
    distance[start] = 0

    while queue:
        v = queue.popleft()
        if distance[v] == k:
            result.append(v)
        for w in graph[v]:
            if distance[w] == -1:
                distance[w] = distance[v] + 1
                queue.append(w)

n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n + 1)]
distance = [-1] * (n + 1)
result = []

for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

bfs(x)
if not len(result):
    print(-1)
else:
    result.sort()
    for x in result:
        print(x)