import sys
input = sys.stdin.readline

def solution(numbers):
    answer = []
    k = sum(numbers) - 100
    n = len(numbers)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if numbers[i] + numbers[j] == k:
                a, b = i, j
                break

    for i in range(n):
        if i == a or i == b:
            continue
        answer.append(numbers[i])

    return answer

numbers = list(map(int, input().split()))
print(*solution(numbers))