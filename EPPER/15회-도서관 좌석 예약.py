def solution(n, s, e):
    arr = []
    for i in range(n):
        arr.append((s[i], e[i]))
    arr.sort(key=lambda x: (x[1]))

    e1, e2 = -1, -1
    cnt = 0

    for start, end in arr:
        if start >= e1:
            e1 = end
            cnt += 1
        elif start >= e2:
            e2 = e1
            e1 = end
            cnt += 1

    return cnt

n = int(input())
s = list(map(int, input().split()))
e = list(map(int, input().split()))

print(solution(n, s, e))