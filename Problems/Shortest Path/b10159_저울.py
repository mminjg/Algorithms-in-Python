import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF]*(n+1) for _ in range(n+1)]

# 플로이드 워셜
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1

for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        # 물건 i에서 j로, 물건 j에서 i로의 경로가 모두 없는 경우 cnt 증가
        if graph[i][j] == INF and graph[j][i] == INF:
            cnt += 1
    print(cnt)

# [2] > [4] 라고 주어진 경우, 방향 그래프로 나타내면 [2]가 [4]를 가리킨다고 생각할 수 있다.
# 즉, 무게가 무거운 물건이 무게가 작은 물건을 가리키는 방향그래프로 나타낼 수 있다.
# 경로로 생각하면, 물건 A에서 물건 B로의 경로가 있다면 물건 A와 물건 B의 비교가 가능한 것이다.
# 플로이드 워셜을 진행한후 물건 i와 물건 j가 비교가 가능한 지 판단하려면 graph[i][j]와 graph[j][j]를 확인하면 된다.
# 비교 결과를 알 수 없는 경우는 graph[i][j]와 graph[j][i]가 모두 INF, 즉 경로가 없는 경우이다.