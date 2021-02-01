import sys
input = sys.stdin.readline

while True:
    stack = []
    result = True
    str = list(input().rstrip())
    if len(str) == 1 and str[0] == '.':
        break

    for x in str:
        if not result:
            break
        if x == '(' or x == '[':
            stack.append(x)
        elif x == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                result = False
        elif x == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                result = False

    if stack:
        result = False

    if result:
        print("yes")
    else:
        print("no")