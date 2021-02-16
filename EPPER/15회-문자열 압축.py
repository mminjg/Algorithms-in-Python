src = input()

before = src[0]

cnt = 0
if before == '1':
    print('1', end='')

for i in range(1, len(src)):
    if before == src[i]:
        cnt += 1
    else:
        print(chr(ord('A') + cnt), end='')
        cnt = 0
        before = src[i]

print(chr(ord('A') + cnt), end='')