import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()  # 정렬
min_s= 2000000001

if n == 2:
    print(arr[0], arr[1])
    exit(0)

for i in range(n - 1):
    start = i + 1
    end = n - 1

    # [i+1, n-1] 의 값 + i번째 값의 합을 비교해나간다.
    while start <= end:
        mid = (start + end) // 2
        s = arr[i] + arr[mid]

        # 혼합 특성값이 0에 가까운 용액을 저장한다.
        if abs(s) < min_s:
            idx1, idx2, min_s = i, mid, abs(s)

        # 혼합 특성값이 0보다 작다면 더 큰 값을 더해주어야 한다.
        if s < 0:
            start = mid + 1
        # 혼합 특성값이 0보다 크다면 더 작은 값을 더해주어야 한다.
        else:
            end = mid - 1

print(arr[idx1], arr[idx2])

# 투포인터x, 이분탐색으로 풀었을 때