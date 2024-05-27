def a(n):
    if n == 0:
        return 0 
    elif n == 1 or n == 2:
        return 1
    else:
        return a(n - 1) + a(n - 2)
    
x = int(input())
print(a(x))