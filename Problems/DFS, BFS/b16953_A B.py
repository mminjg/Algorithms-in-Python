import sys
from collections import deque
input = sys.stdin.readline

a, b = map(int, input().split())

queue = deque()
queue.append((a, 1))

while queue:
    v, cnt = queue.popleft()
    if v > b:
        continue
    if v == b:
        print(cnt)
        exit()
    queue.append((v*2, cnt+1))
    queue.append((10*v+1, cnt+1))

print(-1)