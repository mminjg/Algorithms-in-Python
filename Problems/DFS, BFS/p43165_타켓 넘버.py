def dfs(i, sum_value, target, numbers):
    global answer
    if i == n:
        if sum_value == target:
            answer += 1
        return
    dfs(i + 1, sum_value + numbers[i], target, numbers)
    dfs(i + 1, sum_value - numbers[i], target, numbers)


def solution(numbers, target):
    global answer, n
    n = len(numbers)
    answer = 0
    dfs(0, 0, target, numbers)
    return answer