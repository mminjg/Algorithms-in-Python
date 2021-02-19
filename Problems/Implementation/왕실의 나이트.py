import sys
input = sys.stdin.readline

steps = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

arr = list(input().rstrip())
x, y = int(arr[1]), ord(arr[0])-ord('a')+1

cnt = 0
for step in steps:
    next_x = x + step[0]
    next_y = y + step[1]
    if next_x < 1 or next_x > 8 or next_y < 1 or next_y > 8:
        continue
    cnt += 1
print(cnt)