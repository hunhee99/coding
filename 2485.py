import sys
input = sys.stdin.readline
import math
n = int(input())
g = int(input())
r = g
d = []
cnt = 0
minus_cnt = 1
num = 0
for i in range(1, n):
    num = int(input())
    d.append(num - g)
    g = num
    minus_cnt += 1

a = math.gcd(*d)

for i in d:
    cnt += i//a - 1
print(cnt)