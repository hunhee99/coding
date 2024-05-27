A, B, V = map(int, input().split())
oneday = A - B
V_1 = V - A
if V_1 % oneday == 0:
    print((V_1 // oneday) + 1)
else:
    print((V_1 // oneday) + 2)
