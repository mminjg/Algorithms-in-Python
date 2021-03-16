import sys
input = sys.stdin.readline

def solution(n, money):
    money.insert(0, 0)
    dp = [0] * (n + 1)
    dp[1] = money[1]
    dp[2] = money[1] + money[2]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 3] + money[i - 1] + money[i], dp[i - 2] + money[i], dp[i - 1])

    return dp[n]

n = int(input())
money = list(map(int, input().split()))
print(solution(n, money))

# 최대 연속된 2개까지 가능, 3개부터 불가능
# i-3  i-2  i-1  i
#  O    X    O   O
#       O    X   O
#            O   X
