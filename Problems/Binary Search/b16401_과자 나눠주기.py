import sys
input = sys.stdin.readline

m, n = map(int, input().split())
arr = list(map(int, input().split()))

arr.sort()
end = arr[-1]
start = 0
ans = 0

while start <= end:
    cnt = 0     # mid 길이의 막대과자 개수
    mid = (start + end) // 2
    for i in range(n-1, -1, -1):
        if cnt >= m or arr[i] < mid or mid == 0:
            break
        cnt += arr[i] // mid
    if cnt >= m:
        ans = max(ans, mid)
        start = mid + 1
    else:
        end = mid - 1

print(ans)