a, b, c, d, e, f= map(int, input().split())

if b == 0:
    x = c // a
    y = -(((d * x) - f) / e)
    print(x, int(y))
elif e == 0:
    x = f // d
    y = -(((a * x) - c) / b)
    print(x, int(y))
else:    
    for x in range(-999, 1000):
        if ((a * x) - c) / b == ((d * x) - f) / e:
            y = int(-(((a * x) - c) / b))
            print(x, y)
            break