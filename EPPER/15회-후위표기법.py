import sys

input = sys.stdin.readline

m = int(input())
s = list(input().split())
stack = []

for x in s:
    if x == '*' or x == '/' or x == '+' or x == '-':
        b = stack.pop()
        a = stack.pop()
        if x == '+':
            stack.append(a + b)
        elif x == '-':
            stack.append(a - b)
        elif x == '*':
            stack.append(a * b)
        else:
            stack.append(a // b)
    else:
        stack.append(int(x))

print(stack[0])
