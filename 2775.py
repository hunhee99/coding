t = int(input())

for i in range(t):
    k = int(input())
    n = int(input())
    f = [i for i in range(1, n+1)]
    for j in range(k):
        for l in range(1, n):
            f[l] += f[l-1]
    print(f[-1])