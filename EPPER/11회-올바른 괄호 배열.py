def solve(left, right):
    if left == 0 and right == 0:
        return 1
    else:
        # 왼쪽 괄호 다 사용하고 오른쪽 괄호만 남았을 때,
        # 오른쪽 괄호를 닫는 경우 1
        if left == 0:
            return 1
        # 왼쪽 괄호가 오른쪽 괄호보다 적게 남았을 때,
        # 왼쪽괄호를 사용하거나 오른쪽 괄호 사용 가능
        elif left < right:
            return solve(left - 1, right) + solve(left, right - 1)
        # 왼쪽 괄호와 오른쪽 괄호의 수가 같은 경우,
        # 왼쪽 괄호부터 사용해야 한다.
        else:
            return solve(left - 1, right)

def solution(n):
    return solve(n, n)

n = int(input())
print(solution(n))
