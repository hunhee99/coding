t = int(input())

for i in range(t):
    x_start, y_start, x_stop, y_stop = map(int, input().split())
    n = int(input())
    cnt = 0
    for j in range(n):
        x, y, r = map(int, input().split())
        start = ((x_start - x)**2 + (y_start - y)**2)**0.5
        stop = ((x_stop - x)**2 + (y_stop - y)**2)**0.5
        if start <= r and stop <= r:
            continue
        elif start <= r or stop <= r:
            cnt += 1
    print(cnt)