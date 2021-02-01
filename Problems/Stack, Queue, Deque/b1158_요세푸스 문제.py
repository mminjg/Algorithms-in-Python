import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
result = []
d = deque()
for i in range(1, n+1):
    d.append(i)
    print(d)

idx = 1
while d:
    if idx == k:
        result.append(str(d.popleft()))
        idx = 1
    else:
        d.append(d.popleft())
        idx += 1

print('<', end='')
print(", ".join(result), end='')
print('>')