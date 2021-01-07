import sys

n = int(sys.stdin.readline())
students = list(map(int, sys.stdin.readline().split()))

students.sort()
m = 200001

for i in range(n):
    m = min(m, students[i] + students[-1-i])

print(m)