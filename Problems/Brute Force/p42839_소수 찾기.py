import math
from itertools import permutations

def is_prime(num):
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def solution(numbers):
    numbers = list(numbers)
    arr = []
    answer = []

    for i in range(1, len(numbers) + 1):
        arr.extend(list(map(''.join, permutations(numbers, i))))

    arr.sort()
    arr = [int(x) for x in arr]
    for x in arr:
        if x == 0 or x == 1:
            continue
        if is_prime(x):
            answer.append(x)

    answer = set(answer)

    return len(answer)