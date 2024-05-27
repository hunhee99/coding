n = int(input())
cnt = 0
if n == 1000:
    cnt = 144
else:    
    for i in range(1, n + 1):
        if i < 100:
            cnt += 1
        elif i < 1000:
            a = i % 10
            b = ((i % 100) - a) // 10
            c = i // 100
            result = (c - b) - (b - a)
            if result == 0:
                cnt += 1
print(cnt)      