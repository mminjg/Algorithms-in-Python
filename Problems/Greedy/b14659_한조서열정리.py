import sys

n = int(sys.stdin.readline())
peaks = list(map(int, sys.stdin.readline().split()))

max_h = peaks[0]
max_count = 0
count = 0
for i in range(1, n):
    if peaks[i] < max_h:
        count += 1
    else :
        max_count = max(count, max_count)
        max_h = peaks[i]
        count = 0

if count > max_count:
    max_count = count

print(max_count)