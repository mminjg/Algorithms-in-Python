import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = []
distance = [[INF]*n for _ in range(m)]
for _ in range(m):
    graph.append(list(map(int, input().split())))

if graph[0][0] == -1 or graph[m-1][n-1] == -1:
    print(-1)
    exit()

x, y = 0, 0
q = []
heapq.heappush(q, (graph[x][y], x, y))
distance[x][y] = graph[x][y]

while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
        continue
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= m or ny < 0 or ny >= n:
            continue
        if graph[nx][ny] == -1:
            continue
        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

if distance[m-1][n-1] == INF:
    print(-1)
else:
    print(distance[m-1][n-1])
