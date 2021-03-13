def solution(tickets):
    answer = []
    tickets.sort(reverse=True)
    dc = dict()
    for a, b in tickets:
        if a in dc:
            dc[a].append(b)
        else:
            dc[a] = [b]

    stack = ['ICN']
    while stack:
        top = stack[-1]
        if top not in dc or len(dc[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(dc[top].pop())
    answer.reverse()
    return answer