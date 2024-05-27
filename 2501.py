N, K = map(int, input().split())
arr = []

for i in range(1, N + 1):
    if N % i == 0:
        arr.append(i)
for i in range(K):
    arr.append(0)
print(arr[K - 1])