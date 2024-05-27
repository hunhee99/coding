list_x = []
list_y = []
n = int(input())
if n == 0:
    print(0)
else:
    for i in range(n):
        x, y = map(int, input().split())
        list_x.append(x)
        list_y.append(y)

    result = ((max(list_x) - min(list_x)) * (max(list_y) - min(list_y)))
    print(result)