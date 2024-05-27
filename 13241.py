arr = list(map(int, input().split()))
x = max(arr)
y = 2
while x % min(arr) != 0:
    x = max(arr) * y
    y += 1
print(x)