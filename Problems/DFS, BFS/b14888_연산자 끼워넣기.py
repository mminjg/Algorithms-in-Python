import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

min_value = 10 ** 9
max_value = -10 ** 9

def dfs(i, cur):
    global add, sub, mul, div, max_value, min_value
    if i == n:
        min_value = min(min_value, cur)
        max_value = max(max_value, cur)
    else:
        if add > 0:
            add -= 1
            dfs(i + 1, cur + A[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, cur - A[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, cur * A[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(cur / A[i]))
            div += 1


dfs(1, A[0])

print(max_value)
print(min_value)

# 백트래킹