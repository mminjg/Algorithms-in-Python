import sys
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
F = [0] * 1000001
result = [-1] * n
stack = []

# 오등큰수: 수열 A에서 등장한 횟수가 F(Ai)보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미
# 등장한 횟수 카운트
for num in A:
    F[num] += 1

# 처음 인덱스 넣기
stack.append(0)
i = 1
while stack and i < n:
    while stack and F[A[stack[-1]]] < F[A[i]]:
        result[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
    i += 1

for x in result:
    print(x, end=' ')