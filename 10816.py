import sys
input = sys.stdin.readline
from collections import Counter
N = int(input())
arr = list(map(int, input().split()))

M = int(input())
srr = list(map(int, input().split()))

cnt = Counter(arr)

for i in srr:
    print(cnt[i], end = " ")