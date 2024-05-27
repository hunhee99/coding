a, b = map(int, input().split())
d, c = map(int, input().split())
ja = a * c + b * d
mo = b * c

x = ja
y = mo
while y > 0:
    x, y = y, x % y

print(ja // x, mo // x)