import heapq

def solution(scoville, K):
    cnt = 0
    heapq.heapify(scoville)

    while scoville:
        s1 = heapq.heappop(scoville)
        if s1 >= K:
            break
        if scoville:
            s2 = heapq.heappop(scoville)
            heapq.heappush(scoville, s1 + s2 * 2)
            cnt += 1
        else:
            return -1

    return cnt