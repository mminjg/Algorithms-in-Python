import sys
import copy
from collections import deque
input = sys.stdin.readline


def solution(n, r, goal, N, R):
    graph = [[] for _ in range(N + 1)]
    indegree = [0] * (N + 1)
    q = deque()
    n.insert(0, 0)
    result = copy.deepcopy(n)

    for a, b in r:
        graph[a].append(b)
        indegree[b] += 1

    for i in range(N):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            result[i] = max(result[i], result[now] + n[i])
            indegree[i] -= 1
            if indegree[i] == 0:
                q.append(i)

    return result[goal]


N, R = map(int, input().split())
n = list(map(int, input().split()))
r = []
for _ in range(R):
    a, b = map(int, input().split())
    r.append([a, b])
goal = int(input())

print(solution(n, r, goal, N, R))