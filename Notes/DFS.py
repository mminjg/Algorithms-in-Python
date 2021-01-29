# 인접 리스트로 표현된 그래프에 대한 dfs
# V: 정점 개수, E: 간선 개수
def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for w in graph[v]:
        if not visited[w]:
            dfs(w)

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

# dfs 호출
dfs(v)

# 인접 행렬로 표된 그래프에 대한 dfs
# V: 정점 개수, E: 간선 개수
def dfs(v):
    # 현재 노드를 방문 처리
    visited[v] = True
    print(v, end=' ')
    # 인접 정점을 탐색
    for w in range(1, V + 1):
        # 인접 정점이고, 방문하지 않았으면 dfs
        if graph[v][w] and not visited[w]:
            dfs(w)

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
dfs(v)