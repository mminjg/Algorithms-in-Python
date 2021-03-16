def solution(m, n):
    arr = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = m - n
    kind, num = 0, 0

    i = 0
    while change > 0 and i < 8:
        if change >= arr[i]:
            kind += 1
            num += (change // arr[i])
            change %= arr[i]
        i += 1

    return kind, num

m = int(input())
n = int(input())
print(*solution(m, n))