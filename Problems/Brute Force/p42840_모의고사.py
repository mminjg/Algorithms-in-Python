def solution(answers):
    answer = []
    n = len(answers)
    d1 = [1, 2, 3, 4, 5]
    d2 = [2, 1, 2, 3, 2, 4, 2, 5]
    d3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    result = [0] * 4

    for i in range(n):
        if answers[i] == d1[i%5]:
            result[1] += 1
        if answers[i] == d2[i%8]:
            result[2] += 1
        if answers[i] == d3[i%10]:
            result[3] += 1

    max_value = 0
    for i in range(1, 4):
        if result[i] > max_value:
            max_value = result[i]
            answer = [i]
        elif result[i] == max_value:
            answer.append(i)

    return answer