import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
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

n, e = map(int, input().split())
graph = [[] for _ in range(n+1)]
distance = [INF] * (n+1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())

dijkstra(1)
s_v1 = distance[v1]
s_v2 = distance[v2]

distance = [INF] * (n+1)
dijkstra(v1)
v1_v2 = distance[v2]
v1_n = distance[n]

distance = [INF] * (n+1)
dijkstra(v2)
v2_n = distance[n]
v2_v1 = distance[v1]

result = min(s_v1+v1_v2+v2_n, s_v2+v2_v1+v1_n)
if result >= INF:
    print(-1)
else:
    print(result)