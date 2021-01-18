import sys
input = sys.stdin.readline

def go(i):
    global ans
    if i == n:
        ans += 1
        return

    # 한 행에 퀸 하나씩 가능
    for j in range(n):
        # 열, 우상 대각선, 좌상 대각선
        if not (col[j] or left[i + j] or right[i - j + n - 1]):
            col[j] = left[i + j] = right[i - j + n - 1] = True
            go(i + 1)
            col[j] = left[i + j] = right[i - j + n - 1] = False

n = int(input())
ans = 0

col = [False] * n
left = [False] * (2 * n - 1)
right = [False] * (2 * n - 1)

go(0)
print(ans)