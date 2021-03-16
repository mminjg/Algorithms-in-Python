def solution(n):
    room_num = (n - 1) // 15 + 1
    num = (n - 1) % 15 + 1
    return room_num, num


n = int(input())
print(*solution(n))