
n = int(input())
list_1 = []
list_2 = []
cnt = 0
for i in range(n):
    list_1.append(input())
list_1.append("ENTER")

for i in list_1:
    if i == "ENTER":
        cnt += len(set(list_2))
        list_2 = []
    else:
        list_2.append(i)

print(cnt)