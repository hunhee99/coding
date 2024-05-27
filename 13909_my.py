import sys
input = sys.stdin.readline
n = int(input())
window = [0 for i in range(n)]


for i in range(1, n + 1):
    for j in range(i, n + 1, i):
        if window[j - 1] == 1:
            window[j - 1] = 0
        else:
            window[j - 1] = 1
    
print(sum(window))
        