n = int(input())
f = int(input())
n = n // 100 * 100
while n % f != 0:
    n += 1
print(str(n % 100).zfill(2))
