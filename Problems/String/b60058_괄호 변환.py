def seperate(p):
    cnt1, cnt2 = 0, 0
    u, v = '', ''
    for i in range(len(p)):
        if p[i] == '(':
            cnt1 += 1
        else:
            cnt2 += 1
        if cnt1 == cnt2:
            u = p[:i + 1]
            v = p[i + 1:]
            break
    return u, v


def check_correct(p):
    cnt = 0
    for x in p:
        if x == '(':
            cnt += 1
        else:
            cnt -= 1
            if cnt < 0:
                return False
    return True


def solution(p):
    answer = ''
    if p == '':
        return ''
    u, v = seperate(p)
    print(u, v)
    if check_correct(u):
        answer = u + solution(v)
    else:
        answer += '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1])
        for x in u:
            if x == '(':
                answer += ')'
            else:
                answer += '('
    return answer