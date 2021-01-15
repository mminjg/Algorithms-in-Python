import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))

    d = [[0] * m for _ in range(n)]
    k = 0
    for i in range(n):
        for j in range(m):
            d[i][j] = arr[k]
            k += 1

    for j in range(1, m):
        for i in range(n):
            gold = d[i][j - 1]
            if i - 1 >= 0:
                gold = max(gold, d[i - 1][j - 1])
            if i + 1 < n:
                gold = max(gold, d[i + 1][j - 1])
            d[i][j] += gold

    result = d[0][m - 1]
    for i in range(1, n):
        result = max(result, d[i][m - 1])

    print(result)