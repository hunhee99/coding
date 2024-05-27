A = int(input())
B = int(input())
C = int(input())

arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
list_1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
D = A * B * C
D = str(D)
D = list(D)

for i in range(len(D)):
    D[i] = int(D[i])

for i in D:
    list_1[arr.index(i)] += 1

for i in list_1:
    print(i)