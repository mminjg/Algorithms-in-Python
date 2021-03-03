def solution(clothes):
    dc = dict()
    for x, y in clothes:
        if dc.get(y):
            dc[y] += 1
        else:
            dc[y] = 1

    cnt = 1
    for val in dc.values():
        # 의상종류 + 1 을 곱해주어야 한다. => 안입는 것 고려
        cnt *= (val + 1)

    # (하나는 선택해야 한다)
    return cnt - 1