from statistics import *
import sys
input = sys.stdin.readline

n = int(input())
list_1 = []

for i in range(n):
    list_1.append(int(input()))

print(int(round(mean(list_1),0)))
print(median(list_1))

if len(multimode(list_1)) > 1:
    mode_list = multimode(list_1)
    mode_list.sort()
    print(mode_list[1])
else:
    print(mode(list_1))
print(max(list_1) - min(list_1))
