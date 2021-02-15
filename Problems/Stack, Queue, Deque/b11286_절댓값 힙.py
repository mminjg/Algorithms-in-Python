import sys
import heapq
input = sys.stdin.readline

q = []
n = int(input())
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(q, (abs(x), x))
    else:
        if not q:
            print(0)
        else:
            a, b = heapq.heappop(q)
            print(b)