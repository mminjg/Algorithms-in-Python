import sys
input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()

n = len(a)
m = len(b)

# 2차원 dp 테이블 초기화 **
dp = [[0] * (m + 1) for _ in range(n + 1)]

# dp 테이블 초기 설정 - 빈 문자열을 바꾸기 위해서는 i개의 문자를 삽입해야 하기 때문
for i in range(1, n + 1):
    dp[i][0] = i
for j in range(1, m + 1):
    dp[0][j] = j

# 최소 편집 거리 계산
for i in range(1, n + 1):
    for j in range(1, m + 1):
        # 문자가 같다면, 왼족 위에 해당하는 수 대입
        if a[i - 1] == b[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]
        # 문자가 다르다면, 3가지 경우 중에서 최솟값을 찾는다
        # 3가지 경우 : 삽입, 삭제, 교체
        else:
            dp[i][j] = 1 + min(dp[i][j - 1], dp[i - 1][j], dp[i - 1][j - 1])

print(dp[n][m])