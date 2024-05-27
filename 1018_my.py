N, M = map(int, input().split())
chess_list = []
result = []

b_w = [["B", "W", "B", "W", "B", "W", "B", "W"],
       ["W", "B", "W", "B", "W", "B", "W", "B"],
       ["B", "W", "B", "W", "B", "W", "B", "W"],
       ["W", "B", "W", "B", "W", "B", "W", "B"],
       ["B", "W", "B", "W", "B", "W", "B", "W"],
       ["W", "B", "W", "B", "W", "B", "W", "B"],
       ["B", "W", "B", "W", "B", "W", "B", "W"],
       ["W", "B", "W", "B", "W", "B", "W", "B"]]

w_b = [["W", "B", "W", "B", "W", "B", "W", "B"],
       ["B", "W", "B", "W", "B", "W", "B", "W"],
       ["W", "B", "W", "B", "W", "B", "W", "B"],
       ["B", "W", "B", "W", "B", "W", "B", "W"],
       ["W", "B", "W", "B", "W", "B", "W", "B"],
       ["B", "W", "B", "W", "B", "W", "B", "W"],
       ["W", "B", "W", "B", "W", "B", "W", "B"],
       ["B", "W", "B", "W", "B", "W", "B", "W"]]

error_list = []

for i in range(N):
    arr_1 = input()
    arr_1 = list(arr_1)
    chess_list.append(arr_1)

for i in range(N - 8):
    for j in range(M - 8):
        arr = [row[j : j + 8] for row in chess_list[i : i + 8]]
        result.append(arr)
        
   

for i in range((N - 8) * (M - 8)):
    i_1 = 0
    i_2 = 0
    for j in range(8):
        for k in range(8):
           if result[i][j][k] != b_w[j][k]:
               i_1 += 1
           if result[i][j][k] != w_b[j][k]:
               i_2 += 1  
    error_list.append(i_1)
    error_list.append(i_2)
    
print(error_list)