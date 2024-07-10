a = [list(map(int, input().split())) for _ in range(4)]
b = 0
arr = []
for i in range(4):
    b -= a[i][0]
    b += a[i][1]
    arr.append(b)
print(max(arr))