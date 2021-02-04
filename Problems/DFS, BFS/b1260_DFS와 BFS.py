import sys
from collections import deque
sys.setrecursionlimit(100000)
input = sys.stdin.readline

def dfs(v):
    print(v, end=' ')
    visited[v] = True
    for w in range(1, n+1):
        if graph[v][w] and not visited[w]:
            dfs(w)

def bfs(v):
    queue = deque()
    queue.append(v)
    visited[v] = True

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for w in range(1, n+1):
            if graph[v][w] and not visited[w]:
                queue.append(w)
                visited[w] = True

n, m, v = map(int, input().split())
graph = [[0]*(n+1) for _ in range(n+1)]

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

visited = [False] * (n+1)
dfs(v)
print()

visited = [False] * (n+1)
bfs(v)