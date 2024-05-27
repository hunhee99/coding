N = int(input())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
arr.sort(key=lambda x: (x[1], x[0]))

for i in range(N):
    print(f"{arr[i][0]} {arr[i][1]}")