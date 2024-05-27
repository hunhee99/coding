n, m = map(int, input().split())

arr = dict()


for i in range(n):
    s = input()
    if len(s) >= m:
        if s in arr:
            arr[s] += 1
        else:
            arr[s] = 1




arr = sorted(arr.items(), key = lambda x: (-x[1], -len(x[0]), x[0]))

for i in arr:
    print(i[0])