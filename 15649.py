from itertools import permutations
n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
result = list(permutations(arr, m))

for i in range(len(result)):
    print(*result[i])
    