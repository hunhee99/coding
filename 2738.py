n, m = map(int, input().split())
list_1 = []
list_3 = []
for i in range(n):
    list_2 = list(map(int, input().split()))
    list_1.append(list_2)
for i in range(n):
    list_2 = list(map(int, input().split()))
    list_3.append(list_2)
list_4 = []

for i in range(n):
    arr = []
    for j in range(m):
        
        arr.append(list_1[i][j] + list_3[i][j])
    list_4.append(arr)

for i in range(n):
    for j in range(m):
        print(list_4[i][j], end = ' ')
    print()