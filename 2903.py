n = int(input())
result = 0
r = 2
d = 1
for i in range(n):
    r = r + d
    result = (r)**2
    d = d * 2
print(result)