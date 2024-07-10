t = int(input())
for i in range(t):
    a, b = map(int, input().split())
    if a % 10 == 0:
        print(10)
    else:
        b %= 4
        a %= 10
        if b == 0:
            b = 4
        print(a ** b % 10)