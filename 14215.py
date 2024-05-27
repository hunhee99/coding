a, b, c = map(int, input().split())
list_1 = [a, b, c]

if (sum(list_1) - max(list_1)) <= max(list_1):
    list_1.remove(max(list_1))
    f = sum(list_1) - 1
    list_1.append(f)
    print(sum(list_1))
else:
    print(sum(list_1))
    