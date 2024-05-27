N = int(input())
arr = list(map(int, input().split()))

for i in range(len(arr)):
    list_1 = []
    for j in range(1, arr[i] + 1):
        if arr[i] % j == 0:
            list_1.append(i)
    if len(list_1) == 2:
        arr[i] = 1
    else:
        arr[i] = 0

print(sum(arr))