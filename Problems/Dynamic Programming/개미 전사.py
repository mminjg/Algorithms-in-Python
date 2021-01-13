import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])
for i in range(2, n):
    # i - 1를 공격하면, i는 털지 못함
    # i - 2를 공격하면, i를 털 수 있음
    d[i] = min(d[i - 1], d[i - 2] + arr[i])

print(d[n - 1])