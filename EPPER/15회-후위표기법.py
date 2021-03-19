import sys
input = sys.stdin.readline

def solution(m, s):
    stack = []

    for x in s:
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
                stack.append(a // b)
        else:
            stack.append(int(x))

    return stack[0]

m = int(input())
s = list(input().split())
print(solution(m, s))