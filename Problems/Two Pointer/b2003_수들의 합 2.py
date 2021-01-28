import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

cnt = 0
intervel_sum = 0
end = 0

for start in range(n):
    while intervel_sum < m and end < n:
        intervel_sum += A[end]
        end += 1

    if intervel_sum == m:
        cnt += 1

    intervel_sum -= A[start]

print(cnt)

#2
start = 0
end = 0
while True:
    if intervel_sum >= m:
        intervel_sum -= A[start]
        start += 1
    elif end == n:
        break
    else:
        intervel_sum += A[end]
        end += 1
    if intervel_sum == m:
        cnt += 1