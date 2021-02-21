def solution(s):
    n = len(s)
    result = 1001
    for i in range(1, n+1):
        tmp = ''
        cnt = 1
        before_c = s[:i]
        for j in range(i, n, i):
            c = s[j:j+i]
            print(before_c, c)
            if before_c == c:
                cnt += 1
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
        print(tmp)
        result = min(result, len(tmp))
    return result