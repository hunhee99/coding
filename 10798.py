arr = []

for i in range(5):
    list_1 = map(str, input())
    list_1 = list(list_1)
    while len(list_1) != 15:
        list_1.append(None)
    arr.append(list_1)
    
arr = list(zip(*arr))

for i in range(15):
    for j in range(5):
        if arr[i][j] != None:
            print(arr[i][j], end = "")