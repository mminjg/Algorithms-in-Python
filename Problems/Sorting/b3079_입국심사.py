import sys
input = sys.stdin.readline

n, m = map(int, input().split())
line = [0] * n
for i in range(n):
    line[i] = int(input())

start = 1
end = 10 ** 18
ans = end

while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in range(n):
        total += mid // line[i]
        # 사람 수보다 많으면 break
        if total >= m:
            break
    if total >= m:
        if mid < ans:
            ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)
