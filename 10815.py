import sys
input = sys.stdin.readline


n = int(input())
arr1 = set(map(int, input().split()))
m = int(input())
arr2 = list(map(int, input().split()))

for i in range(m):
    if arr2[i] in arr1:
        print(1, end = " ")
    else:
        print(0, end = " ")
        
