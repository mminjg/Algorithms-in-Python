import sys
from itertools import combinations
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[0] * (n) for _ in range(n)]
house = []
chicken = []
result = int(1e9)

for i in range(n):
    graph[i] = list(map(int, input().split()))
    for j in range(n):
        if graph[i][j] == 1:
            house.append((i, j))
        elif graph[i][j] == 2:
            chicken.append((i, j))

c = list(combinations(chicken, m))

for cc in c:
    total = 0
    for x, y in house:
        tmp = int(1e9)
        # 집에서 가장 가까운 치킨집
        for cx, cy in cc:
            tmp = min(tmp, abs(cx-x)+abs(cy-y))
        total += tmp
    result = min(result, total)

print(result)
