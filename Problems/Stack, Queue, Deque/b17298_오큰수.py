import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
result = [-1] * n
stack = []

stack.append(0)
i = 1
while stack and i < n:
    while stack and A[stack[-1]] < A[i]:
        result[stack[-1]] = A[i]
        stack.pop()

    stack.append(i)
    i += 1

print(*result)