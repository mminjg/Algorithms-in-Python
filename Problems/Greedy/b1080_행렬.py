import sys

n, m = map(int, sys.stdin.readline().split())
a = [[0] * m for _ in range(n)]
b = [[0] * m for _ in range(n)]

for i in range(n):
    a[i] = list(sys.stdin.readline().rstrip())

for i in range(n):
    b[i] = list(sys.stdin.readline().rstrip())

count = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] == b[i][j]:
            continue
        count += 1  # 맨 왼쪽 오른쪽 값이 다르다면 바꿈
        for k in range(i, i+3):
            for l in range(j, j+3):
                if a[k][l] == '0':
                    a[k][l] = '1'
                else:
                    a[k][l] = '0'

for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit(0)

print(count)
