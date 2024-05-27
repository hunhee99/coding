import sys
input = sys.stdin.readline

n = int(input())

for i in range(n):
    arr = list(map(int, input().split()))
    x = max(arr)
    y = 2
    while x % min(arr) != 0:
        x = max(arr) * y
        y += 1
    print(x)