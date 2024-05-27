while True:
    try:
        A, B = map(int, input().split())
        if B % A == 0:
            print("factor")
        elif A % B == 0:
            print("multiple")
        else:
            print("neither")        
    except ZeroDivisionError:
        break