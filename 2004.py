n, m = map(int, input().split())
cnt = 0
l = 1

if m > n//2:
    m = n - m


for i in range(m):
    l *= (n - i)/(i + 1)

while True:
    if l % 10 != 0:
        break
    else:
        l //= 10
        cnt += 1
print(cnt)