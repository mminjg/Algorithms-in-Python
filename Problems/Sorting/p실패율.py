def solution(N, stages):
    answer = []
    rate = []
    user = [0] * (N + 2)

    for i in stages:
        user[i] += 1

    total = len(stages)
    for i in range(1, N + 1):
        if total == 0:
            fail = 0
        else:
            fail = user[i] / total
        rate.append((fail, i))
        total -= user[i]

    rate.sort(key=lambda x:(-x[0], x[1]))

    for i in range(N):
        answer.append(rate[i][1])

    return answer