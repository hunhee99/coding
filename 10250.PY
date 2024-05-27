



t = int(input())

for i in range(t):
    h, w, n = map(int, input().split())
    arr = []
    x, y = 0, 0
    for j in range(h, 0, -1):
        list_1 = []
        for k in range(j, j + (h * (w - 1)) + 1, h):
            list_1.append(k)
        arr.append(list_1)
    for i in range(h):
        for j in range(w):
            if arr[i][j] == n:
                x = i
                y = j
                
    
    arr_1 = [[0 for i in range(w)] for j in range(h)]
    f = 1
    for j in range(h - 1 , -1, -1):
        
        room = 100 * f + 1
        for k in range(w):
            
            arr_1[j][k] += room
            room += 1
        f += 1    
        
    print(arr_1[x][y])

    
        
    
    