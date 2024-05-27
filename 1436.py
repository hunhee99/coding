N = int(input())
list_666 = []
k = 666
while len(list_666) <= N:
    if "666" in str(k):
        list_666.append(k)
    k += 1
print(list_666[N - 1])