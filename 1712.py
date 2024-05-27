import sys
input = sys.stdin.readline

a, b, c = map(int, input().split())
d = c - b
if d <= 0:
    print(-1)
else:
    z = a // d + 1
    print(z)