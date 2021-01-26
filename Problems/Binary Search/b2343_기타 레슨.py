import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)
end = sum(arr)
ans = end

while start <= end:
    mid = (start + end) // 2    # 가장 작은 큰 레슨 시간 합
    s = 0
    cnt = 0

    # 레슨시간을 더해가며 블루레이 개수를 센다.
    for i in range(n):
        if s + arr[i] > mid:
            cnt += 1
            s = 0
        s += arr[i]
    # 레슨이 남았다면 블루레이 + 1
    if s > 0:
        cnt += 1

    if cnt > m:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)

