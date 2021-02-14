import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

# 상하좌우 이동
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

m, n = map(int, input().split())
graph = []
distance = [[INF] * m for _ in range(n)]
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

# 시작 위치 초기화
x, y = 0, 0
q = []
heapq.heappush(q, (0, x, y))
distance[x][y] = 0

while q:
    dist, x, y = heapq.heappop(q)
    # 이미 처리된 경우
    if distance[x][y] < dist:
        continue
    # 상하좌우 인접한 노드 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >= m:
            continue
        cost = dist + graph[nx][ny]
        if cost < distance[nx][ny]:
            distance[nx][ny] = cost
            heapq.heappush(q, (cost, nx, ny))

print(distance[n-1][m-1])