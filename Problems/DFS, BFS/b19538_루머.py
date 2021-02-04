import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
time = [-1] * (n+1)

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in arr:
        if j != 0:
            graph[i].append(j)

m = int(input())
arr = list(map(int, input().split()))
tmp = []

queue = deque()
for v in arr:
    queue.append((v, 0))
    time[v] = 0

while queue:
    v, s = queue.popleft()
    for w in graph[v]:
        cnt = 0
        total = 0
        if time[w] == -1:
            for k in graph[w]:
                if time[k] != -1:
                    cnt += 1
                total += 1
            if total != 0 and cnt/total >= 0.5:
                tmp.append(w)

    if not queue:
        while tmp:
            w = tmp.pop()
            time[w] = s+1
            queue.append((w, s+1))

for i in range(1, n+1):
    print(time[i], end=' ')