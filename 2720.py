def c_to_qdnp(x):
    q =25
    d = 10
    n = 5
    p = 1
    arr = []
    arr.append(x // q)
    x = x % q
    arr.append(x // d)
    x = x % d
    arr.append(x // n)
    x = x % n
    arr.append(x // p)
    x = x % p
    return arr

t = int(input())

for i in range(t):
    C = int(input())
    print(*c_to_qdnp(C))
    