n = int(input())
p = 1
for i in range(1, n + 1):
    p *= i
p = str(p)
p = p[::-1]
c = 0
for i in p:
    if i == '0':
        c += 1
    else:
        break

print(c)