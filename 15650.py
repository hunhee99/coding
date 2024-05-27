from itertools import combinations
n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
result = list(combinations(arr, m))

for i in range(len(result)):
    print(*result[i])
    