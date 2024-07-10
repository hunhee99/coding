n, m = map(int, input().split())
a = [0]
for i in range(46):
    for j in range(i):
        a.append(i)
print(sum(a[n:m + 1]))