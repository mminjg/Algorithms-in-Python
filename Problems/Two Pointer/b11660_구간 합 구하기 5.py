import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pre = [[0] * (n+1) for _ in range(n+1)]

for i in range(1, n+1):
    arr = list(map(int, input().split()))
    for j in range(1, n+1):
        pre[i][j] = pre[i][j-1]+pre[i-1][j]-pre[i-1][j-1] + arr[j-1]

for i in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(pre[x2][y2]-pre[x1-1][y2]-pre[x2][y1-1]+pre[x1-1][y1-1])

# 구간 합 사용시 pre[i-1]를 사용함으로 처음 배열을 잡을 때 1~n까지로 설정해야한다.