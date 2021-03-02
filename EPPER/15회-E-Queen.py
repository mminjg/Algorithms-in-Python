# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys
input = sys.stdin.readline

def check(a, b):
    for i in range(k):
        if x[i] == a and y[i] == b:
            return True
    return False

def go(i):
    global ans
    if i == n + 1:
        ans += 1
        return

    for j in range(1, n + 1):
        if check(i, j):
            continue
        if not (col[j] or left[i + j] or right[i - j + n - 1]):
            col[j] = left[i + j] = right[i - j + n - 1] = True
            go(i + 1)
            col[j] = left[i + j] = right[i - j + n - 1] = False


n = int(input())
k = int(input())
ans = 0

col = [False] * (n + 1)
left = [False] * (2 * n + 1)
right = [False] * (2 * n + 1)

x = list(map(int, input().split(',')))
y = list(map(int, input().split(',')))

go(1)
print(ans)