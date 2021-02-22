import sys
from collections import deque
input = sys.stdin.readline

# 반시계 방향
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

# d 방향으로 다음칸
def go():
    global sec, x, y
    nx = x + dx[d]
    ny = y + dy[d]
    # 머리가 벽에 닿았을 때
    if nx < 1 or nx > n or ny < 1 or ny > n:
        print(sec+1)
        exit()
    # 머리가 자신의 몸과 닿았을 때
    if graph[nx][ny] == -1:
        print(sec+1)
        exit()
    q.append((nx, ny))
    # 사과가 있으면 사과 없애고 자신 몸
    if graph[nx][ny] == 1:
        graph[nx][ny] = -1
    # 사과가 없을 때 몸 줄임
    elif graph[nx][ny] == 0:
        graph[nx][ny] = -1
        tx, ty = q.popleft()
        graph[tx][ty] = 0
    x, y = nx, ny
    sec += 1

n = int(input())
k = int(input())
graph = [[0]*(n+1) for _ in range(n+1)]
info = []

for _ in range(k):
    a, b = map(int, input().split())
    graph[a][b] = 1

l = int(input())
for _ in range(l):
    a, b = input().split()
    info.append((int(a), b))

q = deque()
x, y = 1, 1
graph[x][y] = -1
q.append((x, y))
sec = 0
d = 0
idx = 0

while True:
    if idx < l and sec == info[idx][0]:
        if info[idx][1] == 'L':
            d = (d+1) % 4
        else:
            d = (d-1) % 4
        idx += 1
    go()