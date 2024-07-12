def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def find_k(M, N, x, y):
    k = x
    while k <= lcm(M, N):
        if (k - 1) % N + 1 == y:
            return k
        k += M
    return -1

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().split())
    # y가 N이면 0으로 조정 (N으로 나눌 때 나머지가 0이기 때문)
    y_adjusted = y if y != n else 0
    result = -1
    # x와 같은 나머지를 갖는 k를 구하는 loop
    for i in range(x, lcm(m, n) + 1, m):
        if i % n == y_adjusted:
            result = i
            break
    print(result)
