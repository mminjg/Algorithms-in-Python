import sys

input = sys.stdin.readline

numbers = list(map(int, input().split()))
total = sum(numbers)
k = total - 100

for i in range(8):
    for j in range(i + 1, 9):
        if numbers[i] + numbers[j] == k:
            a, b = i, j
            break

for i in range(9):
    if i == a or i == b:
        continue
    print(numbers[i], end=' ')
