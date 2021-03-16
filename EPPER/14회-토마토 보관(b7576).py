import sys
from collections import deque
input = sys.stdin.readline

def solution(n, m, graph):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    result = 0

    # 익은 토마토 큐에 삽입
    q = deque()
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                q.append((i, j, 0))

    # 인접 토마토 확인
    while q:
        x, y, day = q.popleft()
        result = max(result, day)

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if graph[nx][ny] == -1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                q.append((nx, ny, day + 1))

    # 모든 토마토 확인
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                return -1

    return result

n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
print(solution(m, n, graph))