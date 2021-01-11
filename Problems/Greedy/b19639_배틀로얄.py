import sys
input = sys.stdin.readline
x, y, m = map(int, input().split())

enemy = [0] * x
heal = [0] * y
result = []

for i in range(x):
    enemy[i] = int(input())

for i in range(y):
    heal[i] = int(input())

# 투 포인터로 접근
idx1 = 0
idx2 = 0
curm = m

# m // 2 지점을 기준으로 적 or 아이템 결정해야 한다
while idx1 < x or idx2 < y:
    # 현재 체력이 m / 2보다 크고 남은 적이 있을 경우
    if idx1 < x and curm > m // 2:
        result.append(-(idx1 + 1))
        curm -= enemy[idx1]
        idx1 += 1
    # 현재 체력이 m / 2보다 작거나 같고 남은 아이템이 있을 경우
    elif idx2 < y and curm <= m // 2:
        result.append(idx2 + 1)
        curm += heal[idx2]
        idx2 += 1
    else:
        break

while idx1 < x or idx2 < y:
    # 남은 적이 있을 경우
    if idx1 < x:
        result.append(-(idx1 + 1))
        curm -= enemy[idx1]
        idx1 += 1
    # 남은 아이템이 있을 경우
    elif idx2 < y:
        result.append(idx2 + 1)
        curm += heal[idx2]
        idx2 += 1

if curm <= 0:
    print(0)
else:
    for x in result:
        print(x)