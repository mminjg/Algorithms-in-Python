import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(1, n+1)]
target = list(map(int, input().split()))

d = deque(arr)

cnt = 0
for t in target:
    for i in range(len(d)):
        if d[i] == t:
            dif = i
    if dif <= len(d) - dif:
        for j in range(dif):
            d.append(d.popleft())
        d.popleft()
        cnt += dif
    else:
        dif = len(d) - dif
        for j in range(dif):
            d.appendleft(d.pop())
        d.popleft()
        cnt += dif

print(cnt)