import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

# n * n 영역 체크
def check(a, b, n):
    if 10 - a >= n and 10 - b >= n:
        for i in range(a, a+n):
            for j in range(b, b+n):
                if arr[i][j] == 0:
                    return False
        return True
    return False

# 영역을 t로 바꾸기
def change(a, b, n, t):
    for i in range(a, a+n):
        for j in range(b, b+n):
            arr[i][j] = t

def go(i, j, cnt):
    global answer
    # 다음 행으로
    if j == 10:
        go(i+1, 0, cnt)
        return
    # 종료
    if i == 10:
        answer = min(answer, cnt)
        return
    # 0이면 다음으로
    if arr[i][j] == 0:
        go(i, j+1, cnt)
        return
    # 1이면 영역 처리
    for n in range(5, 0, -1):
        if paper[n] > 0 and check(i, j, n):
            change(i, j, n, 0)
            paper[n] -= 1
            go(i, j+1, cnt+1)
            change(i, j, n, 1)
            paper[n] += 1

arr = [[] for _ in range(10)]
paper = [0, 5, 5, 5, 5, 5]
answer = 26

for i in range(10):
    arr[i] = list(map(int, input().split()))

go(0, 0, 0)
if answer == 26:
    print(-1)
else:
    print(answer)