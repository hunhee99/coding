

c = int(input())
for i in range(c):
    arr = list(map(int, input().split()))
    n = arr.pop(0)
    mean = sum(arr) / n
    high = []
    for j in arr:
        if j > mean:
            high.append(j)
    per = (len(high) / len(arr)) * 100
    print(f"{per:.3f}%")