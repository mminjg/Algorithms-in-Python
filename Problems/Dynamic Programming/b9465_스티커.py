# 첫 번째 풀이
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    arr = [[0] * n for _ in range(2)]
    dp = [[0] * n for _ in range(2)]

    for i in range(2):
        arr[i] = list(map(int, input().split()))

    dp[0][0] = arr[0][0]
    dp[1][0] = arr[1][0]

    for j in range(1, n):
        for i in range(2):
            if i == 0:
                dp[i][j] = dp[1][j - 1] + arr[i][j]
            elif i == 1:
                dp[i][j] = dp[0][j - 1] + arr[i][j]
            if j - 2 >= 0 and i == 0:
                dp[i][j] = max(dp[i][j], dp[1][j - 2] + arr[i][j])
            elif j - 2 >= 0 and i == 1:
                dp[i][j] = max(dp[i][j], dp[0][j - 2] + arr[i][j])

    mx = dp[0][0]
    for i in range(2):
        mx = max(mx, max(dp[i]))

    print(mx)


# 두 번째 풀이 => 불필요한 for, max 줄이기
import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())

    dp = [[0] * n for _ in range(2)]

    for i in range(2):
        dp[i] = list(map(int, input().split()))

    dp[0][1] += dp[1][0]
    dp[1][1] += dp[0][0]

    for j in range(2, n):   # 범위를 2부터로 수정
        dp[0][j] += max(dp[1][j - 1], dp[1][j - 2])
        dp[1][j] += max(dp[0][j - 1], dp[0][j - 2])

    print(max(dp[0][n - 1], dp[1][n - 1]))