n = int(input())
arr = list(map(int, input().split()))

arr2 = list(set(arr))
arr2.sort()

dic = {arr2[i] : i for i in range(len(arr2))}

for i in arr:
    print(dic[i], end = " ")