def make_arr():
    n = int(input())
    a = []

    for i in range(n):
        a.append([n//2 - i, n//2 + i])
    return a

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


n = int(input())
for x in range(n):
    a = make_arr()
    for i in range(len(a)):
        if is_prime(a[i][0]) and is_prime(a[i][1]):
            print(a[i][0], a[i][1])
            break
