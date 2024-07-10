n = int(input())
arr_1 = []
arr_2 = ['*' for _ in range(n)]
for i in range(n):
    arr_3 = arr_1 + arr_2
    print(''.join(arr_3))
    arr_1.append(' ')
    arr_2.pop()