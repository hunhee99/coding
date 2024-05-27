n, k = map(int, input().split())
arr = [i for i in range(1, n + 1)]
stack = 0
s = []
while arr:
    stack += k - 1
    if stack >= len(arr):
        stack %= len(arr)
    s.append(str(arr.pop(stack)))
        
print("<", ", ".join(s), ">", sep="")