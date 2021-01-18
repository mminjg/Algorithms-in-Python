import sys
input = sys.stdin.readline

n, k = map(int, input().split())

dp = [[0] * (k + 1) for _ in range(n + 1)]
v = [0] * n
w = [0] * n

for i in range(n):
    w[i], v[i] = map(int, input().split())

mx = 0
for i in range(1, n + 1):
    for j in range(1, k + 1):
        if w[i - 1] <= j:   # 현재 물건을 배낭에 넣을 수 있는 경우
            dp[i][j] = max(v[i - 1] + dp[i - 1][j - w[i - 1]], dp[i - 1][j])
        else:   # 현재 물건을 배낭에 넣을 수 없을 경우
            dp[i][j] = dp[i - 1][j]

    mx = max(mx, max(dp[i]))

print(mx)