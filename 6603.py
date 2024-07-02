from itertools import combinations

while True:
    k = list(map(int, input().split()))
    if k == [0]:
        break
    a = k[1:]
    b = combinations(a, 6)
    for i in b:
        print(' '.join(map(str, i)))
    print()