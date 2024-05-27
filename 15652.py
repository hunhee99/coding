from itertools import combinations_with_replacement as com
n, m = map(int, input().split())

arr = [i for i in range(1, n + 1)]
result = list(com(arr, m))

for i in range(len(result)):
    print(*result[i])
    