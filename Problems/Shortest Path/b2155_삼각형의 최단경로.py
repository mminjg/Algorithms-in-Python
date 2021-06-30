import sys
import math
import heapq
input = sys.stdin.readline
INF = int(1e9)

start, end = map(int, input().split())
n = max(start, end)
while True:
    if math.sqrt(n) == int(math.sqrt(n)):
        break
    n += 1

dt = [-2, -1, +1]
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

i = 3
k = 1
while i < n:
    for a in range(i, i+2*k, 2):
        for t in dt:
            b = a + t
            graph[a].append((b, 1))
            graph[b].append((a, 1))
    i = a + 3
    k += 1
    dt[0] = -2 * k

q = []
heapq.heappush(q, (0, start))
distance[start] = 0

while q:
    dist, now = heapq.heappop(q)
    if distance[now] < dist:
        continue
    for i in graph[now]:
        cost = dist + i[1]
        if cost < distance[i[0]]:
            distance[i[0]] = cost
            heapq.heappush(q, (cost, i[0]))

print(distance[end])