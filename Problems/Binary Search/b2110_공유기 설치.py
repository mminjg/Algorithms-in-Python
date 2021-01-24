import sys
input = sys.stdin.readline

n, c = map(int, input().split())

arr = [0] * n
for i in range(n):
    arr[i] = int(input())

arr.sort()

# 최대 최소 거리(가장 인접한 두 공유기 사이의 거리 gap)
start = 1   # 가능한 최소 거리
end = arr[-1] - arr[0]  # 가능한 최대 거리
result = 0

while start <= end:
    mid = (start + end) // 2
    val = arr[0]
    cnt = 1     # 맨 처음 공유기

    # 공유기 앞에서부터 설치
    for i in range(1, n):
        if arr[i] >= val + mid:
            val = arr[i]
            cnt += 1

    # c개이상 설치할 수 있는지 확인
    if cnt >= c:    # 설치할 수 있는 경우 gap 증가시킨다.
        start = mid + 1
        result = mid
    else:   # 설치할 수 없는 경우 gap을 감소시킨다.
        end = mid - 1

print(result)