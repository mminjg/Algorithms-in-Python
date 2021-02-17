def solve(left, right):
    #
    if left == 0 and right == 0:
        return 1
    else:
        # 왼쪽 괄호 다 사용, 오른쪽 괄호만 남았을 때
        if left == 0:
            return 1
        # 왼쪽 괄호가 오른쪽 괄호보다 적게 남았을 떼
        elif left < right:
            return solve(left - 1, right) + solve(left, right - 1)
        # 왼쪽 괄호와 오른쪽 괄호의 수가 같은 경우
        else:
            return solve(left - 1, right)

n = int(input())
print(solve(n, n))
