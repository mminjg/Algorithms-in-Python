import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())

graph = [[0] * n for _ in range(n)]
second = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
start = []

for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if graph[i][j] != 0:
            start.append((graph[i][j], i, j))

s, target_x, target_y = map(int, input().split())

# 번호가 낮은 종류부터 증식, 큐에 낮은 번호부터 삽입하고 시작해야 한다**
start.sort()
queue = deque(start)

while queue:
    virus, x, y = queue.popleft()

    if second[x][y] == s:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue

        if graph[nx][ny] == 0:
            graph[nx][ny] = virus
            second[nx][ny] = second[x][y] + 1
            queue.append((virus, nx, ny))

print(graph[target_x-1][target_y-1])