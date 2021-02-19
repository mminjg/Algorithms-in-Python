import sys
input = sys.stdin.readline

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
type = ['L', 'R', 'U', 'D']

n = int(input())
arr = list(map(str, input().split()))

x, y = 1, 1
for plan in arr:
    for i in range(4):
        if plan == type[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 1 or nx > n or ny < 1 or ny > n:
                continue
            x, y = nx, ny

print(x, y)