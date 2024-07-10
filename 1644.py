import math

def get_primes(n):
    # n 이하의 모든 소수를 찾기 위해 에라토스테네스의 체를 사용합니다.
    if n < 2:
        return []
    
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False  # 0과 1은 소수가 아닙니다.
    
    for start in range(2, int(math.sqrt(n)) + 1):
        if sieve[start]:
            for multiple in range(start * start, n + 1, start):
                sieve[multiple] = False
    
    # 소수 리스트 반환
    return [num for num, is_prime in enumerate(sieve) if is_prime]




n = int(input())
prime = get_primes(n)
cnt = 0


for i in range(len(prime)):
    for j in range(i, len(prime)):
        if sum(prime[i:j+1]) > n:
            break
        if sum(prime[i:j+1]) == n:
            cnt += 1

print(cnt)