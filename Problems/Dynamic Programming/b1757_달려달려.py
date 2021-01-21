import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = [0] * (n + 1)
# 3차원 dp, dp[x][y][z] x분에 y 지침지수, z 뛰는지/쉬는지 에서의 달린거리 최댓값
dp = [[[0] * 2 for _ in range(m + 5)] for _ in range(n + 5)]

for i in range(1, n + 1):
    arr[i] = int(input())

for i in range(1, n + 1):
    for j in range(m + 1):
        if j != 1:
            if j:   # j가 1보다 크다면
                dp[i][j][1] = dp[i-1][j-1][1] + arr[i]  # 달린다
                dp[i][j][0] = max(dp[i-1][j+1][1], dp[i-1][j+1][0]) # 쉰다
            else:   # j가 0이라면 쉬어야 한다. 0일때 쉬어도 0
                dp[i][j][0] = max(dp[i-1][j+1][0], dp[i-1][j+1][1], dp[i-1][j][0])
        else:
            dp[i][j][1] = max(dp[i-1][j-1][1], dp[i-1][j-1][0]) + arr[i]
            dp[i][j][0] = max(dp[i-1][j+1][1], dp[i-1][j+1][0])

print(dp[n][0][0])