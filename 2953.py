a = 0
score = 0
for i in range(1, 6):
    arr = list(map(int, input().split()))
    if sum(arr) > score:
        a = i
        score = sum(arr)
print(a, score)