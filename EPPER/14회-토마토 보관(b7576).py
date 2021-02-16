import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m = map(int, input().split())
graph = [[] for _ in range(m)]
arr = []

for i in range(m):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if graph[i][j] == 1:
            arr.append((i, j, 0))

min_day = 0
q = deque(arr)
while q:
    x, y, day = q.popleft()
    min_day = day
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == -1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 1
            q.append((nx, ny, day + 1))

for i in range(m):
    for j in range(n):
        if graph[i][j] == 0:
            print(-1)
            exit()

print(min_day)
