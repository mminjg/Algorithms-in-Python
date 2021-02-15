import sys
input = sys.stdin.readline
INF = int(1e9)

def bf(start):
    dist[start] = 0
    for i in range(n):
        for j in range(2*m+w):
            cur, next_node, cost = edges[j]
            if dist[cur] + cost < dist[next_node]:
                dist[next_node] = dist[cur] + cost
                if i == n - 1:
                    return True
    return False

tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    edges = []
    dist = [INF] * (n + 1)
    for i in range(m):
        s, e, t = map(int, input().split())
        edges.append((s, e, t))
        edges.append((e, s, t))
    for i in range(w):
        s, e, t = map(int, input().split())
        edges.append((s, e, -t))
    negative_cycle = bf(1)

    if negative_cycle:
        print("YES")
    else:
        print("NO")