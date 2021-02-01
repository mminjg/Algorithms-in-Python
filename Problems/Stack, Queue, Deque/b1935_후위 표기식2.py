import sys
input = sys.stdin.readline

n = int(input())
f = list(input().rstrip())
num = [0] * n
stack = []

for i in range(n):
    num[i] = int(input())

for x in f:
    # 연산자
    if x == '+' or x == '-' or x == '*' or x == '/':
        b = stack.pop()
        a = stack.pop()

        if x == '+':
            stack.append(a + b)
        elif x == '-':
            stack.append(a - b)
        elif x == '*':
            stack.append(a * b)
        else:
            stack.append(a / b)
    # 피연산자
    else:
        stack.append(num[ord(x)-65])

print("%.2f" % stack[-1])