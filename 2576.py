cnt = 0
min_odd = 999999999

for _ in range(7):
    n = int(input())
    if n % 2 != 0:
        cnt += n
        if n < min_odd:
            min_odd = n
if cnt == 0:
    print(-1)
else:
    print(cnt)
    print(min_odd)