import sys
import copy
from collections import deque

input = sys.stdin.readline

n, r = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]
time = list(map(int, input().split()))
time.insert(0, 0)

for _ in range(r):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

target = int(input())

result = copy.deepcopy(time)

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)

while q:
    now = q.popleft()
    for i in graph[now]:
        result[i] = max(result[i], result[now] + time[i])
        indegree[i] -= 1
        if indegree[i] == 0:
            q.append(i)

print(result[target])
