import heapq

INF = int(1e9)

def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    distance = [INF] * (n + 1)

    for a, b in edge:
        graph[a].append((b, 1))
        graph[b].append((a, 1))

    q = []
    heapq.heappush(q, (0, 1))
    distance[1] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    cnt = 0
    max_value = 0
    for i in range(1, n + 1):
        if distance[i] > max_value:
            max_value = distance[i]
            cnt = 1
        elif distance[i] == max_value:
            cnt += 1

    return cnt