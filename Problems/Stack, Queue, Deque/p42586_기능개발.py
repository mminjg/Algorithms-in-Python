def solution(progresses, speeds):
    answer = []
    n = len(progresses)

    for i in range(n):
        if (100 - progresses[i]) % speeds[i] == 0:
            progresses[i] = (100 - progresses[i]) // speeds[i]
        else:
            progresses[i] = (100 - progresses[i]) // speeds[i] + 1

    i = 0
    while i < n:
        cnt = 1
        for j in range(i + 1, n):
            if progresses[j] <= progresses[i]:
                cnt += 1
            else:
                break
        answer.append(cnt)
        i += cnt
    return answer