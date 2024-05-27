N = int(input())
M = int(input())
arr = []
for i in range(N, M + 1):
    list_1 = []
    for j in range(1, i + 1):
        if i % j == 0:
            list_1.append(j)
    if len(list_1) == 2:
        arr.append(i)

if len(arr) >= 1:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)