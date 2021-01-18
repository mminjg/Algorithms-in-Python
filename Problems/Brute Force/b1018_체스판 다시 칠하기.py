import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [[]] * n

for i in range(n):
    arr[i] = list(input().rstrip())

min = 64
for yi in range(n - 8 + 1):
    for xj in range(m - 8 + 1):
        count = 0
        for y in range(8):
            for x in range(8):
                ct = ''
                if (xj + x + yi + y) % 2 == 0:
                    ct = 'W'
                else:
                    ct = 'B'
                # 색이 다르면 count 증가
                if arr[yi + y][xj + x] != ct:
                    count += 1
        # 다른 체스판도 고려해야 한다.
        if 64 - count < count:
            count = 64 - count
        if count < min:
            min = count

print(min)