N, M = map(int, input().split())
arr = list(map(int, input().split()))
sum_0 = []
sum_1 = []
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            sum_0.append(arr[i] + arr[j] + arr[k])
for i in sum_0:
    if i <= M:
        sum_1.append(i)


print(max(sum_1))
