from itertools import combinations

n, m = map(int, input().split())
a = list(map(str, input().split()))
a.sort()
b = combinations(a, n)

for i in b:
    count_1 = 0
    count_2 = 0
    for j in i:
        if j in ['a', 'e', 'i', 'o', 'u']:
            count_1 += 1
        else:
            count_2 += 1
    if count_1 >= 1 and count_2 >= 2:
        print(''.join(i))