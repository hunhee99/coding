from math import factorial

n, k = map(int, input().split())
a = factorial(n) // (factorial(k) * factorial(n - k))
print(a % 10007)