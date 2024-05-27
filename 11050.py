import sys
from math import comb
input = sys.stdin.readline

n, m = map(int, input().split())
print(comb(n,m))