import sys
input = sys.stdin.readline
import math

def is_prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


number = [x for x in range(1, 123456 * 2 + 1)]
prime_num = []
for i in number:
    if is_prime(i):
        prime_num.append(i)


while True:
    N = int(input())
    if N == 0:
        break
    result = 0
    for i in prime_num:
        if N < i <= 2 * N:
            result += 1
    print(result)
    