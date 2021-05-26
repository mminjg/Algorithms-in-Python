import sys
from collections import deque
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 2

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 2

tc = int(input())
for _ in range(tc):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]
    temp = []
    cnt = 0

    for i in range(k):
        y, x = map(int, input().split())
        graph[x][y] = 1
        temp.append((x, y))

    for x, y in temp:
        if graph[x][y] == 1:
            bfs(x, y)
            cnt += 1

    print(cnt)
