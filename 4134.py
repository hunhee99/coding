import sys
import math
input = sys.stdin.readline

def prime(x):
    if x == 0 or x == 1:
        return False
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True


n = int(input())

for i in range(n):
    a = int(input())
    while True:
        if prime(a) == True:
            print(a)
            break
        a += 1