import sys
from collections import deque
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n = int(input())
    indegree = [0] * (n + 1)
    graph = [[False] * (n + 1) for i in range(n + 1)]

    t = list(map(int, input().split()))
    for i in range(n):
        for j in range(i + 1, n):
            graph[t[i]][t[j]] = True
            indegree[t[j]] += 1

    m = int(input())
    for i in range(m):
        a, b = map(int, input().split())
        if graph[a][b]:
            graph[a][b] = False
            graph[b][a] = True
            indegree[b] -= 1
            indegree[a] += 1
        else:
            graph[b][a] = False
            graph[a][b] = True
            indegree[a] -= 1
            indegree[b] += 1

    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    flag = True     # 위상 정렬 결과가 오직 하나인지
    cycle = False   # 그래프 내 사이클이 존재하는지

    for i in range(n): # 노드 개수만큼
        # 사이클 발생
        if len(q) == 0:
            cycle = True
            break
        # 가능한 정렬결과가 여러개
        if len(q) >= 2:
            flag = False
            break
        now = q.popleft()
        result.append(now)
        for i in range(1, n + 1):
            if graph[now][i]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    q.append(i)

    if cycle:
        print("IMPOSSIBLE")
    elif not flag:
        print("?")
    else:
        print(*result)