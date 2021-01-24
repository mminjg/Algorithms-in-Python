import heapq


def solution(food_times, k):
    n = len(food_times)
    # 전체 시간보다 k가 같거나 크다면 남은 음식이 존재하지 않는다.
    if sum(food_times) <= k:
        return -1
    q = []
    for i in range(n):
        heapq.heappush(q, (food_times[i], i + 1))  # 시간과 번호를 우선순위 큐에 삽입

    time = 0
    pre_time = 0
    length = n

    while time + ((q[0][0] - pre_time) * length) <= k:
        now = heapq.heappop(q)[0]
        time += (now - pre_time) * length
        length -= 1
        pre_time = now

    result = sorted(q, key=lambda x: x[1])  # 음식의 번호 기준으로
    return result[(k - time) % length][1]

    return answer