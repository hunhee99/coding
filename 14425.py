import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr1 = []
arr2 = []
cnt = 0

for i in range(n):
    arr1.append(input())

for i in range(m):
    arr2.append(input())

arr1 = set(arr1)

for i in arr2:
    if i in arr1:
        cnt += 1
print(cnt)