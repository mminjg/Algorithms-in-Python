import sys
input = sys.stdin.readline

g = int(input())
n = 200001
arr = [0] * (n+1)
ans = []

for i in range(1, n+1):
    arr[i] = i * i

end = 1
start = 1
while True:
    if end >= n:
        break
    dif = arr[end] - arr[start]
    if dif < g:
        end += 1
    if dif > g:
        start += 1
    if dif == g:
        ans.append(end)
        end += 1

if not len(ans):
    print(-1)
else:
    for x in ans:
        print(x)