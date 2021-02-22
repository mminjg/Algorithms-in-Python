def solution(s):
    n = len(s)
    result = 1001
    # i 단위로 자른다.
    for i in range(1, n+1):
        tmp = ''    # 단위가 i 일 때 압축한 문자열
        cnt = 1     # 압축할 때 숫자 카운트
        before_c = s[:i]    # 중복 확인을 위한 before
        # i부터 i 단위로 자름
        for j in range(i, n, i):
            c = s[j:j+i]
            # 전과 중복되는 경우
            if before_c == c:
                cnt += 1
            # 전과 중복되지 않은 경우
            else:
                if cnt == 1:
                    tmp += before_c
                else:
                    tmp += (str(cnt)+before_c)
                cnt = 1
                before_c = c
        if cnt == 1:
            tmp += before_c
        else:
            tmp += (str(cnt)+before_c)
        # 가장 짧은 길이의 값을 result로
        result = min(result, len(tmp))
    return result