a = list(map(int, input().split()))
b = [0, 0, 0]
cnt = 0
while b != a:
    b[0] += 1
    if b[0] == 16:
        b[0] = 1
    b[1] += 1
    if b[1] == 29:
        b[1] = 1
    b[2] += 1
    if b[2] == 20:
        b[2] = 1
    cnt += 1
print(cnt)