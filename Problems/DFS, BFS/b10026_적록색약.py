import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# 적록색약이 아닌 사람
def dfs1(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == graph[x][y] and not visited[nx][ny]:
            dfs1(nx, ny)

# 적록색약인 사람
def dfs2(x, y):
    visited[x][y] = True
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if visited[nx][ny]:
            continue
        if graph[x][y] == 'R' or graph[x][y] == 'G':
            if graph[nx][ny] == 'R' or graph[nx][ny] == 'G':
                dfs2(nx, ny)
        else:
            if graph[x][y] == graph[nx][ny]:
                dfs2(nx, ny)

n = int(input())
graph = []
cnt1 = 0
cnt2 = 0

for i in range(n):
    graph.append(list(input().rstrip()))

visited = [[False]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs1(i, j)
            cnt1 += 1

visited = [[False] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            dfs2(i, j)
            cnt2 += 1

print(cnt1, cnt2)