import sys
from itertools import combinations
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if tmp[nx][ny] == 0:
                tmp[nx][ny] = 2
                queue.append((nx, ny))

n, m = map(int, input().split())
graph = [[0] * m for _ in range(n)]
tmp = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
data = []
virus = []
mx = 0

for i in range(n):
    graph[i] = list(map(int, input().split()))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            data.append((i, j))
        elif graph[i][j] == 2:
            virus.append((i, j))

# 3개의 벽을 세우는 경우의 수
walls = list(combinations(data, 3))

# 벽 세우는 모든 경우, 바이러스 퍼질 때
for wall in walls:
    # tmp로 graph 복사
    for i in range(n):
        for j in range(m):
            tmp[i][j] = graph[i][j]
    # 벽 세우기
    for i in range(3):
        tmp[wall[i][0]][wall[i][1]] = 1
    # virus bfs
    for x in virus:
        bfs(x[0], x[1])
    # 안전 영역 크기 구하기
    cnt = 0
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == 0:
                cnt += 1
    mx = max(mx, cnt)

print(mx)