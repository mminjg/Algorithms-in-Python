def solution(s):
    answer = ''
    n = len(s)
    cnt = 0
    before = s[0]

    # '1'로 시작하는 문자열일 경우
    if before == '1':
        answer += '1'

    for i in range(1, n):
        # 이전과 같은 경우 cnt 추가
        if s[i] == before:
            cnt += 1
        # 이전과 다른 경우 cnt 만큼 등장한 해당 문자 추가
        else:
            answer += chr(ord('A') + cnt)
            before = s[i]
            cnt = 0

    answer += chr(ord('A') + cnt)
    return answer

s = input()
answer = solution(s)
print(answer)