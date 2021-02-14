import sys
from collections import deque
input = sys.stdin.readline

n = int(input())    # 컴퓨터의 수
m = int(input())    # 간선의 수

# 그래프와 방문 리스트 초기화
graph = [[0]*(n+1) for _ in range(n+1)]
visited = [False] * (n+1)
cnt = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

# bfs
queue = deque()
# 1부터 시작
queue.append(1)
visited[1] = True

while queue:
    v = queue.popleft()
    visited[v] = True
    # 바이러스 걸리는 컴퓨터 수 증가
    cnt += 1
    for w in range(1, n+1):
        # 인접하고 방문하지 않았으면
        if graph[v][w] and not visited[w]:
            queue.append(w)
            visited[w] = True

# 1번 빼고 바이러스 걸리게 되는 컴퓨터 수 출력
print(cnt-1)