import sys

def power(base, exponent, modulus):
    result = 1
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        base = (base * base) % modulus
        exponent //= 2
    return result

a, b, c = map(int, sys.stdin.readline().split())
print(power(a, b, c))