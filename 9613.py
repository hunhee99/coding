def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


n = int(input())


for i in range(n):
    a = list(map(int, input().split()))
    result = 0
    for i in range(1, len(a)):
        for j in range(i+1, len(a)):
            result += gcd(a[i], a[j])
    print(result)