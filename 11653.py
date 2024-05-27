N = int(input())
arr = []
list_1 = []
for i in range(1, N + 1):
    if N % i == 0:
        arr.append(i)

for i in arr:
    list_2 = []
    for j in range(1, i + 1):
        if i % j == 0:
            list_2.append(i)
    if len(list_2) <= 2:
        list_1.append(i)

if N != 1:
    for i in list_1:
        if i == 1:
            continue
        while N % i == 0:
            N = N // i
            print(i)