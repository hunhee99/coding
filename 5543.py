price = []

for i in range(5):
    price.append(int(input()))
print(min(price[:3]) + min(price[3:]) - 50)