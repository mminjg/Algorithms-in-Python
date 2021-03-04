def solution(brown, yellow):
    sum_value = (brown - 4) // 2
    for x in range(1, sum_value + 1):
        y = sum_value - x
        if x * y == yellow:
            if x >= y:
                return [x+2, y+2]
            else:
                return [y+2, x+2]