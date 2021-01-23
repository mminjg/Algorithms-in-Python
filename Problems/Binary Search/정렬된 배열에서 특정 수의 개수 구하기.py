import sys
import bisect
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

a = bisect.bisect_left(arr, x)
b = bisect.bisect_right(arr, x)
if b - a == 0:
    print(-1)
else:
    print(b - a)