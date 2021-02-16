import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

k = int(input())
for _ in range(E):
    # u에서 v로 가는 가중치 w
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

# 다익스트라 진행
def dijkstra(start):
    q = []
    # 시작 노드의 최단 경로는 0
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)
        # 이미 처리된 적 있는 경우 continue
        if distance[now] < dist:
            continue
        # 현재 노드와 인접한 노드 확인
        for i in graph[now]:
            cost = dist + i[1]
            # 현재 노드를 거쳐 이동하는 경우가 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(k)

for i in range(1, V+1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
