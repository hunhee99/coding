n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(str, input().split())))
    arr[i][0] = int(arr[i][0])
arr.sort(key = lambda x: (x[0]))

for i in range(n):
    print(*arr[i])