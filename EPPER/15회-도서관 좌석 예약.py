n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))

arr = []
for i in range(n):
    arr.append((s[i], e[i]))

if n <= 2:
    print(n)
    exit()

arr.sort(key=lambda x: (x[1]))

e1, e2 = -1, -1
cnt = 0
for i in range(n):
    s = arr[i][0]
    if arr[i][0] >= e1:
        cnt += 1
        e1 = arr[i][1]
    elif arr[i][0] >= e2:
        # e1을 먼저 배정
        e2 = e1
        e1 = arr[i][1]
        cnt += 1

print(cnt)
