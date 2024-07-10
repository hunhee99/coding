arr = list(map(int, input().split()))
time = int(input())
h = time // 3600
time %= 3600
m = time // 60
time %= 60
s = time
arr[0] += h
arr[1] += m
arr[2] += s

if arr[2] >= 60:
    arr[2] %= 60
    arr[1] += 1
if arr[1] >= 60:
    arr[1] %= 60
    arr[0] += 1
if arr[0] >= 24:
    arr[0] %= 24
print(arr[0], arr[1], arr[2])