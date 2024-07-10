l, p = map(int, input().split())
l *= p
arr = list(map(int, input().split()))
for i in range(len(arr)):  # 수정된 부분
    arr[i] = arr[i] - l
print(*arr)