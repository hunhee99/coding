arr = list(map(int, input().split()))
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = list(reversed(list_1))

if arr == list_1:
    print("ascending")
elif arr == list_2:
    print("descending")
else:
    print("mixed")