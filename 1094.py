x = int(input())
stick = [64, 32, 16, 8, 4, 2, 1]
count = 0


for i in stick:
    if x >= i:
        x -= i
        count += 1
    if x == 0:
        break

print(count)