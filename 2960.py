n, k = map(int, input().split())

arr = []
for i in range(2, n+1):
    for j in range(1, n//i+1):
        if i*j not in arr:
            arr.append(i*j)
        elif i*j > n:
            break
print(arr[k-1])