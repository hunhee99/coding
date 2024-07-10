N = int(input())
s = 1
cnt = 0
while N >= s:

    N -= s
    s += 1
    cnt += 1
print(cnt)