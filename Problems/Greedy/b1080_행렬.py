import sys

n, m = map(int, sys.stdin.readline().split())
# 행렬 a, b n * m 초기화
a = [[0] * m for _ in range(n)]
b = [[0] * m for _ in range(n)]

for i in range(n):
    a[i] = list(sys.stdin.readline().rstrip())

for i in range(n):
    b[i] = list(sys.stdin.readline().rstrip())

# 맨 위쪽의 왼쪽 값은 한번 확인하면 더이상 고려하지 않아도 된다.
count = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] == b[i][j]:  # 같다면 다음으로
            continue
        # 다르다면 3*3크기의 부분행렬에 있는 모든 원소를 뒤집어야 한다.
        count += 1
        for k in range(i, i+3):
            for l in range(j, j+3):
                if a[k][l] == '0':
                    a[k][l] = '1'
                else:
                    a[k][l] = '0'

# 행렬 a와 행렬 b가 같은지 확인한다.
for i in range(n):
    for j in range(m):
        if a[i][j] != b[i][j]:
            print(-1)
            exit(0)

print(count)
