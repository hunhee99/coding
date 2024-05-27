n = int(input())

if n < 10:
    n *= 10
p = n
cnt = 0
while True:    
    a = p // 10
    b = p % 10
    c = a + b
    if c >= 10:
        c = c % 10
    p = b * 10 + c
    cnt += 1
    if n == p:
        break
print(cnt)