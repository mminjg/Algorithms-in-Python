import sys
input = sys.stdin.readline

def go(idx):
    if idx == len(zero):
        for i in range(9):
            for j in range(9):
                print(arr[i][j], end=' ')
            print()
        exit(0)
        return

    x, y = zero[idx][0], zero[idx][1]
    check = [False] * 10

    for i in range(9):  # 한 열에 있는 숫자 체크
        check[arr[i][y]] = True
    for j in range(9):  # 한 행에 있는 숫자 체크
        check[arr[x][j]] = True
    for i in range(x // 3 * 3, x // 3 * 3 + 3):  # 3*3 정사각형 안에 있는 숫자 체크
        for j in range(y // 3 * 3, y // 3 * 3 + 3):
            check[arr[i][j]] = True

    # 3가지 조건을 만족하는 숫자가 있으면 다음 0으로
    flag = False
    for i in range(1, 10):
        if not check[i]:
            flag = True
            arr[x][y] = i
            go(idx + 1)
            arr[x][y] = 0

    # 적절한 숫자가 없으면
    if not flag:
        return

arr = [[]] * 9
for i in range(9):
    arr[i] = list(map(int, input().split()))

# 0인 좌표를 저장하는 수열 초기화
zero = []
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            zero.append([i, j])
go(0)