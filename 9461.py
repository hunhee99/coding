arr = [1, 1, 1, 2, 2, 3, 4, 5, 7 ,9]
for i in range(100):
    arr.append(arr[-1] + arr[-5])
n = int(input())
for i in range(n):
    print(arr[int(input()) - 1])