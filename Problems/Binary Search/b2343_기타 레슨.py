import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = list(map(int, input().split()))

start = max(arr)    # 최소는 가장 큰 레슨 시간이다.
end = sum(arr)      # 최대는 모든 레슨시간의 합이다.
ans = end

while start <= end:
    mid = (start + end) // 2    # mid = 가능한 블루레이 크기
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

    # 블루레이 개수가 m보다 크다면 가능한 블루레이 크기를 증가시켜야 한다.
    if cnt > m:
        start = mid + 1

    # 블루레이 개수가 m보다 작거나 같다면 가능한 블루레이의 크기를 감소시켜야 한다.
    # mid 값을 저장한다.
    else:
        ans = mid
        end = mid - 1

print(ans)

