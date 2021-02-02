import sys
input = sys.stdin.readline

# 숫자인지 판단하는 함수
def is_number(s):
    if s == '(' or s == ')' or s == '[' or s == ']':
        return False
    return True

stack = []
str = list(input().rstrip())
n = len(str)
i = 0

for x in str:
    if x == '(' or x == '[':
        stack.append(x)
    elif x == ')':
        sum_value = 0
        while True:
            if not stack:   # 스택이 비었으면 올바르지 못함
                print(0)
                exit()
            if is_number(stack[-1]):    # 숫자면 sum_value에 더해줌
                sum_value += stack.pop()
            elif stack[-1] == '(':
                stack.pop()
                if sum_value == 0:  # (인데 괄호안에 다른 괄호가 없다면 2, 있으면 sum_value * 2
                    sum_value = 1
                stack.append(2*sum_value)
                break
            elif stack[-1] == '[':
                print(0)
                exit()
    elif x == ']':
        sum_value = 0
        while True:
            if not stack:  # 스택이 비었으면 올바르지 못함
                print(0)
                exit()
            if is_number(stack[-1]):  # 숫자면 sum_value에 더해줌
                sum_value += stack.pop()
            elif stack[-1] == '[':
                stack.pop()
                if sum_value == 0:  # [인데 괄호안에 다른 괄호가 없다면 3, 있으면 sum_value * 3
                    sum_value = 1
                stack.append(3 * sum_value)
                break
            elif stack[-1] == '(':
                print(0)
                exit()

sum_value = 0
while stack:
    # 스택에 괄호가 남았으면 틀림
    if not is_number(stack[-1]):
        print(0)
        exit(0)
    sum_value += stack.pop()
print(sum_value)
