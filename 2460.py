a = []
b = []
for i in range(10):
    c, d = map(int, input().split())
    a.append(c)
    b.append(d)
f = 0 + sum(a) - sum(b)

max = 0
for i in range(10):
    f += b[i] - a[i]
    if f > max:
        max = f

print(max)