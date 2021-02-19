import sys
input = sys.stdin.readline

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
visited = [[False] * m for _ in range(n)]
x, y, d = map(int, input().split())
visited[x][y] = True

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def turn_left():
    global d
    d -= 1
    if d == -1:
        d = 3

cnt = 1
check = 0
while True:
    turn_left()
    nx = x + dx[d]
    ny = y + dy[d]

    if graph[nx][ny] == 0 and not visited[nx][ny]:
        visited[nx][ny] = True
        x, y = nx, ny
        cnt += 1
        check = 0
        continue
    else:
        check += 1

    if check == 4:
        nx = x - dx[d]
        ny = y - dy[d]
        if graph[nx][ny] == 1:
            break
        else:
            x, y = nx, ny
        check = 0

print(cnt)
