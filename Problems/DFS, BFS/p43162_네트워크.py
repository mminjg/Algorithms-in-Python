def dfs(v, computers, visited, n):
    visited[v] = True
    for w in range(n):
        if v != w and computers[v][w] and not visited[w]:
            dfs(w, computers, visited, n)


def solution(n, computers):
    answer = 0
    visited = [False] * n

    for i in range(n):
        if not visited[i]:
            dfs(i, computers, visited, n)
            answer += 1
    return answer