import sys
input = sys.stdin.readline

real_prime = [False, False] + [True] * 999999
for i in range(2, 1000001):
    if real_prime[i]:
        for j in range(i*2, 1000001, i):
            real_prime[j] = False


T = int(input())

for i in range(T):
    cnt = 0
    n = int(input())  
    for j in range(2, n//2 + 1):
        if real_prime[j] and real_prime[n - j]:
            cnt += 1     
    print(cnt)