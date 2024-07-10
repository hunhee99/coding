t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    result = 1
    for j in range(n):
        a, b = input().split()
        arr.append(b)
    arr_1 = list(set(arr))
    for k in arr_1:
        result *= (arr.count(k) + 1)
    print(result - 1)