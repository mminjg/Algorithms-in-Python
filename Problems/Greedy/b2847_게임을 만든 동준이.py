import sys

n = int(sys.stdin.readline())

scores = [0] * n
for i in range(n):
    scores[i] = int(sys.stdin.readline())

count = 0
for i in range(n-1, 0, -1): # 뒤에서부터
    if scores[i-1] >= scores[i]:
        t = scores[i-1] - scores[i] + 1
        scores[i-1] -= t
        count += t

print(count)