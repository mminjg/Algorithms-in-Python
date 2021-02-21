import sys
input = sys.stdin.readline

arr = list(input().rstrip())
arr.sort()

total = 0
for x in arr:
    if x.isalpha():
        print(x, end='')
    else:
        total += int(x)

print(total)
