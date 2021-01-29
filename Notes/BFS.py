from collections import deque
# 인접 리스트로 표현된 그래프에 대한 bfs
# V: 정점 개수, E: 간선 개수
def bfs(start):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소를 하나 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 인접하고, 방문하지 않은 원소를 큐에 삽입
        for w in graph[v]:
            if not visited[w]:
                queue.append(w)
                visited[w] = True

# 그래프 초기화
graph = [[] for _ in range(V + 1)]
# 방문 리스트 초기화
visited = [False] * (V + 1)

# 그래프 간선 입력받기
for i in range(E):
    a, b = map(int, sys.stdin.readline().split())
    # 가중치가 없는 무향 그래프
    graph[a].append(b)
    graph[b].append(a)

# bfs 호출
bfs(v)


from collections import deque
# 인접 행렬로 표현된 그래프에 대한 bfs
# V: 정점 개수, E: 간선 개수
def bfs(start):
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        # 큐에서 원소를 하나 뽑아 출력
        v = queue.popleft()
        print(v, end=' ')
        # 해당 원소와 인접하고, 방문하지 않은 원소를 큐에 삽입
        for w in range(1, V + 1):
            if graph[v][w] and not visited[w]:
                queue.append(w)
                visited[w] = True

# 그래프 초기화
graph = [[0] * (V + 1) for _ in range(V + 1)]
# 방문 리스트 초기화
visited = [False] * (V + 1)

# 그래프 간선 입력받기
for i in range(E):
    a, b = map(int, sys.stdin.readline().split())
    # 가중치가 없는 무향 그래프
    graph[a][b] = 1
    graph[b][a] = 1

# dfs 호출
bfs(v)