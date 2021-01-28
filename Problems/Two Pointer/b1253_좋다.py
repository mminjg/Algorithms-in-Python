import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
A.sort()

cnt = 0
for i in range(n):
    target = A[i]
    # 양쪽에서 접근
    start = 0
    end = n - 1

    while True:
        if start == i:
            start += 1
        if end == i:
            end -= 1
        if start >= end:
            break

        s = A[start] + A[end]
        if s < target:
            start += 1
        elif s > target:
            end -= 1
        else:
            cnt += 1
            break

print(cnt)