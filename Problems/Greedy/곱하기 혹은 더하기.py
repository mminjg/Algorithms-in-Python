import sys

s = sys.stdin.readline().rstrip()

n = len(s)
result = int(s[0])

for i in range(1, n):
    num = int(s[i])
    if num <= 1 or result <= 1: # 1일 때도 고려해야 한다.
        result += num
    else:
        result *= num

print(result)