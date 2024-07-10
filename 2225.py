from math import factorial

def comb(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))

n, k = map(int, input().split())
n += 1
k -= 1

# 중복 조합의 수 계산
result = comb(n + k - 1, k)
print(result % 1000000000)
