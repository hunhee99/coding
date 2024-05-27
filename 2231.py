N = int(input())
OneZero = 0
for i in range(1, N):
    arr = str(i)
    arr = list(arr)
    result = i
    for j in arr:
        result += int(j)
    if result == N:
        print(i)
        OneZero = 1
        break
if OneZero == 0:
    print(OneZero)