a = 300
b = 60
c = 10
n = int(input())
a_n = n // a
n %= a
b_n = n // b
n %= b
c_n = n // c
if n % c != 0:
    print(-1)
else:
    print(a_n, b_n, c_n)