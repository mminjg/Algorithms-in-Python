import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
visited = [False] * 100001

queue = deque()
queue.append((n, 0))
visited[n] = True

while queue:
    x, s = queue.popleft()
    if x == k:
        print(s)
        exit()

    x1 = x - 1
    x2 = x + 1
    x3 = x * 2
    if x1 >= 0 and not visited[x1]:
        queue.append((x1, s+1))
        visited[x1] = True
    if x2 <= 100000 and not visited[x2]:
        queue.append((x2, s+1))
        visited[x2] = True
    if x3 <= 100000 and not visited[x3]:
        queue.append((x3, s+1))
        visited[x3] = True
